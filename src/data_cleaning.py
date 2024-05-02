import pandas as pd

df = pd.read_csv('../preprocessed_data/minutes.csv')


def count_zeros(df):
    # Count the number of occurrences of 0.0 or 0 in each column
    zeros_count = ((df == 0.0) | (df == 0)).sum()
    return zeros_count

def count_missing_values(df):
    missing_values = df.isnull().sum()
    return missing_values


def fill_na_with_zero(df, column):
    """
    Replaces all NaN (missing) values in a column with 0.

    Parameters:
    df (pandas.DataFrame): Input DataFrame
    column (str): Name of the column

    Returns:
    pandas.DataFrame: DataFrame with NaN values replaced by 0 in the specified column
    """
    df[column].fillna(0, inplace=True)
    return df

def interpolate_missing_values(df):
    """
    Interpolates missing values in all columns of a DataFrame.

    Parameters:
    df (pandas.DataFrame): Input DataFrame

    Returns:
    pandas.DataFrame: DataFrame with missing values interpolated
    """
    interpolated_df = df.copy()  # copy to avoid modifications on the original DataFrame
    for column in df.columns:
        if column.lower() != 'heartrate':
            interpolated_df[column] = df[column].interpolate(method='linear')
    return interpolated_df



count_zeros_column = count_zeros(df)
print(count_zeros_column)

na_values = count_missing_values(df)
print(na_values)

# df = fill_na_with_zero(df, 'sleep')
# interpolated_df = interpolate_missing_values(df)


