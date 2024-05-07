import pandas as pd
import re

df = pd.read_csv('../preprocessed_data/minutes.csv')

def select_data(df):
    """
        implements functionality for users to select specific subjects and time periods

        Parameters:
        df (pandas.DataFrame): Input DataFrame

        Returns:
        pandas.DataFrame: DataFrame with desired subjects and time period specified by the user
    """
    #print(df.head())

    column_names = df.columns.tolist()
    values_to_remove = ['DateTime', 'Month', 'Day', 'WeekDay', 'Hour']
    column_names = [x for x in column_names if x not in values_to_remove]
    print("List of subjects to select from: ", column_names)

    # prompts user to select subject(s) and splits the input into a list of subjects
    user_subjects = input("Please select one or more subjects\n").lower()
    user_subjects = re.split(r'[,\s;|]+', user_subjects)
    print(user_subjects)

    wrong_input = True
    while wrong_input:

        # filters columns based on user's subject selection
        matching_columns = [col for col in df.columns if col.lower() in user_subjects]
        print(matching_columns)

        if len(matching_columns) != len(user_subjects):
            # prompts user to select subject(s) again if selected subjects do not match column names
            print("The selected subjects don't match with the column names of the dataframe.")
            user_subjects = input("Please select again\n").lower()
            user_subjects = re.split(r'[,\s;|]+', user_subjects)
        else:
            wrong_input = False

    # generates subset of DataFrame based on selected subjects
    selected_subset = df[matching_columns]
    selected_subset = selected_subset.join(df['DateTime'])

    date_range = (df['DateTime'].min(), df['DateTime'].max())
    print("DateTime range:", date_range)

    out_of_range = True
    while out_of_range:
        # prompts the user to select a time period within the DateTime range
        user_start = input("Please select a starting time period within the DateTime range\n")
        user_end = input("Please select an ending time period within the DateTime range\n")

        min = df['DateTime'].min()
        max = df['DateTime'].max()

        # checks if the selected time range is valid
        if ((user_start >= min) & (user_end <= max) &
                ((user_end >= user_start) & (user_end <= max))):
            out_of_range = False
        else:
            print("Selected time period is false or outside the DateTime range.")
            print("Min DateTime", min)
            print("Max DateTime", max)

    # filters rows based on user's time period selection
    filtered_subset = selected_subset[(selected_subset['DateTime'] >= user_start) &
                                      (selected_subset['DateTime'] <= user_end)]


    return filtered_subset


print(select_data(df))



