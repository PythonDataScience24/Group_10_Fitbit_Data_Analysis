import pandas as pd
from IPython.display import display

df = pd.read_csv('../data/Custom_Dataframes/DailyActivity.csv')

#print(df.to_string())


# number of occurrences of 0.0 or 0 in each column of the DataFrame
def count_zeros_in_columns(df):
    # Count the number of occurrences of 0.0 or 0 in each column
    count_zeros_column = ((df == 0.0) | (df == 0)).sum()
    return count_zeros_column


# if row has only 0.0- or 0-value in each column remove from DataFrame
def remove_rows_with_zeros(df):
    # checks if any row contains only 0.0 or 0 values in each column
    has_zeros_rowwise = (df.eq(0.0) | df.eq(0)).all(axis=1)

    # DataFrame is filtered to keep rows where at least one value is not 0.0 or 0
    df_filtered = df[~has_zeros_rowwise]

    return df_filtered

# definition of outliers

