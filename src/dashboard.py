"""
This module is responsible for creating a dashboard using Dash.
The user can select the subjects, the plot type, the date range, and the resolution of the data to be shown.
"""

from datetime import date
import os
from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../preprocessed_data/minutes.csv'))
df['DateTime'] = pd.to_datetime(df['DateTime'])

app.layout = html.Div([
    html.H1(children='FitBit Dashboard', style={'textAlign': 'center'}),
    html.Div([
        dcc.Dropdown(options=df['Id'].unique(),
                     value=[6117666160, 5577150313, 6775888955],
                     multi=True,
                     id='subject-selection', className="four columns"),
        dcc.Dropdown(
            id='plot-type-selection',
            options=[
                {'label': 'Line Plot', 'value': 'line'},
                {'label': 'Bar Chart', 'value': 'bar'},
                {'label': 'Scatter Plot', 'value': 'scatter'}
            ],
            value='line', className="two columns"),
        dcc.DatePickerRange(
            id='date-picker-range',
            display_format='DD.MM.Y',
            first_day_of_week=1,
            min_date_allowed=date(2016, 3, 11),
            max_date_allowed=date(2016, 5, 12),
            initial_visible_month=date(2016, 3, 11),
            className="four columns"
        ),
        dcc.Dropdown(['Minutes', 'Hours', 'Days', 'Weeks', 'Months'],
                     value='Days',
                     id='resolution-selection',
                     className="two columns"),
    ], className="container"),

    html.Div([
        html.H2(children='Steps', style={'textAlign': 'center'}),
        dcc.Graph(id='steps-graph'),
    ]),

    html.Div([
        html.H2(children='Calories', style={'textAlign': 'center'}),
        dcc.Graph(id='calories-graph'),
    ]),

    html.Div([
        html.H2(children='Intensity', style={'textAlign': 'center'}),
        dcc.Graph(id='intensity-graph'),
    ]),

    html.Div([
        html.H2(children='Sleep', style={'textAlign': 'center'}),
        dcc.Graph(id='sleep-graph'),
    ]),

    html.Div([
        html.H2(children='Heartrate', style={'textAlign': 'center'}),
        dcc.Graph(id='heartrate-graph'),
    ]),

    html.Div([
        html.H2(children='Summary Statistics', style={'textAlign': 'center'}),
        html.Div([
            dcc.Dropdown(
                ['Steps', 'Calories', 'Intensity', 'Sleep', 'Heartrate'],
                value='Steps',
                id='metrics-selection',
                style={'width': '60%', 'margin': 'auto', 'padding': '10px'}
            ),
            dash_table.DataTable(
                id='summary-statistics-table',
                columns=[
                    {"name": "Metric", "id": "metric"},
                    {"name": "Total", "id": "total"},
                    {"name": "Mean", "id": "mean"},
                    {"name": "Median", "id": "median"}
                ],
                style_cell={
                    'textAlign': 'center',
                    'padding': '10px',
                    'font-family': 'Arial, sans-serif',
                    'whiteSpace': 'normal',
                    'height': 'auto',
                },
                style_header={
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'fontWeight': 'bold',
                    'font-family': 'Arial, sans-serif',
                },
                style_table={
                    'margin': 'auto',
                    'padding': '20px',
                    'border': '1px solid black',
                    'borderRadius': '10px',
                    'boxShadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2)',
                }
            )
        ], style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center', 'marginTop': '20px'})
    ])

])


@callback(
    [
        Output('steps-graph', 'figure'),
        Output('calories-graph', 'figure'),
        Output('intensity-graph', 'figure'),
        Output('sleep-graph', 'figure'),
        Output('heartrate-graph', 'figure'),
        Output('summary-statistics-table', 'data')
    ],
    [
        Input('plot-type-selection', 'value'),  # Include the plot type input
        Input('subject-selection', 'value'),
        Input('date-picker-range', 'start_date'),
        Input('date-picker-range', 'end_date'),
        Input('resolution-selection', 'value'),
        Input('metrics-selection', 'value'),

    ]
)
def update_steps(plot_type, subject, date_range_start, date_range_end, resolution, metric):
    """
    Updates the plots based on the selected values.
    This method is called when any of the inputs in the callback changes.

    :param plot_type: The selected plot type
    :param subject: The selected subjects
    :param date_range_start: The start date of the range
    :param date_range_end: The end date of the range
    :param resolution: The selected resolution
    :return: A list of plots to add to the outputs
    """

    try:
        dff = select_subject(df, subject)
        dff = select_date_range(dff, date_range_start, date_range_end)
        dff = select_resolution(dff, resolution)

        dff['Id'] = pd.Categorical(dff['Id'])

        summary_statistics = calculate_summary_statistics(dff, metric)

        # Dictionary of plot functions
        plot_functions = {
            'line': px.line,
            'bar': px.bar,
            'scatter': px.scatter
        }

        if plot_type in plot_functions:
            plot_function = plot_functions[plot_type]

            # Generate plots using the selected plot function for each metric
            return (
                plot_function(dff, x='DateTime', y='Steps', color='Id'),
                plot_function(dff, x='DateTime', y='Calories', color='Id'),
                plot_function(dff, x='DateTime', y='Intensity', color='Id'),
                plot_function(dff, x='DateTime', y='Sleep', color='Id'),
                plot_function(dff, x='DateTime', y='Heartrate', color='Id'),
                summary_statistics
            )
    except Exception as e:
        # If plot_type is invalid, return None for all plots
        print("Error: ", e)
        error_message = f"There is an Error while loading the plots, please refresh the site <br> <br> Error Message: {e}"
        error_figure = {'data': [], 'layout': {'title': {'text': error_message, 'font': {'size': 40, 'color': 'red'}}}}
        return error_figure, None, None, None, None, None


def calculate_summary_statistics(dff, metric):
    """
    Calculates the summary statistics for the given metric.

    :param dff: The DataFrame to calculate the statistics on
    :param metric: The metric to calculate the statistics for
    :return: The summary statistics
    """
    metrics = ['Steps', 'Calories', 'Intensity', 'Sleep', 'Heartrate']
    if metric in metrics:
        mean_value = dff[metric].mean()
        median_value = dff[metric].median()
        total_value = dff[metric].sum()

        summary_statistics = [{
            "metric": metric,
            "total": f"{total_value:.2f}",
            "mean": f"{mean_value:.2f}",
            "median": f"{median_value:.2f}"
        }]

    return summary_statistics



def select_subject(dff, subject):
    """
    Selects the subject based on the given value.

    :param subject: The subject to select
    :return: The selected subject
    """
    return dff[dff['Id'].isin(subject)]


def select_date_range(dff, date_range_start, date_range_end):
    """
    Filters the DataFrame based on the selected date range.
    If no date range is selected, the default range is used.

    :param dff: The dateframe to filter on
    :param date_range_start: The start date of the range
    :param date_range_end: The end date of the range
    :return: The filtered DataFrame
    """
    if date_range_start is None:
        date_range_start = '2016-03-11'
    if date_range_end is None:
        date_range_end = '2016-05-12'

    date_range_start = pd.to_datetime(date_range_start)
    date_range_end = pd.to_datetime(date_range_end)

    return dff[(pd.to_datetime(dff['DateTime']) >= date_range_start)
               & (pd.to_datetime(dff['DateTime']) <= date_range_end)]


def select_resolution(dff, resolution):
    """
    Selects the resolution based on the given value.

    :param resolution: The resolution to select
    :return: The selected resolution
    """

    if resolution == 'Hours':
        return dff.groupby(['Id', pd.Grouper(key='DateTime', freq='h')]).sum().reset_index()
    if resolution == 'Days':
        return dff.groupby(['Id', pd.Grouper(key='DateTime', freq='D')]).sum().reset_index()
    if resolution == 'Weeks':
        return dff.groupby(['Id', pd.Grouper(key='DateTime', freq='W')]).sum().reset_index()
    if resolution == 'Months':
        return dff.groupby(['Id', pd.Grouper(key='DateTime', freq='ME')]).sum().reset_index()

    # minutes is the default resolution
    return dff


if __name__ == '__main__':
    app.run(debug=True)
