import pandas as pd
import re

from src.data_pre_processor import DataPreProcessor


class DataSelection:

    def __init__(self):
        #self.df_minutes = DataPreProcessor()
        #self.df_selected = self.df_minutes.load_pickle_to_dataframe()
        self.df_selected = pd.read_csv('../preprocessed_data/minutes.csv')
        pass

    def select_data(self):

        self.display_columns()

        # generates subset of DataFrame based on selected subjects
        matching_columns = self.select_subjects()
        selected_subset = self.df_selected[matching_columns]
        selected_subset = selected_subset.join(self.df_selected['DateTime'])

        self.display_time_range()
        self.df_selected = self.select_time_range(selected_subset)


    def save_selected_data(self):
        """
        Save the merged dataframe to a CSV and pickle file.
        The pickle is a binary file that can be used to save the dataframe including indexes.
        """
        print("Saving merged dataframe to CSV and pickle...")
        self.df_selected.to_csv("../preprocessed_data/selected_minutes.csv")
        self.df_selected.to_pickle("../preprocessed_data/selected_minutes.pkl")

    def display_columns(self):
        column_names = self.df_selected.columns.tolist()
        values_to_remove = ['DateTime', 'Month', 'Day', 'WeekDay', 'Hour']
        column_names = [x for x in column_names if x not in values_to_remove]
        print("List of subjects to select from: ", column_names)

    def select_subjects(self):
        # prompts user to select subject(s) and splits the input into a list of subjects
        user_subjects = input("Please select one or more subjects\n").lower()
        user_subjects = re.split(r'[,\s;|]+', user_subjects)
        print(user_subjects)

        wrong_input = True
        while wrong_input:

            # filters columns based on user's subject selection
            matching_columns = [col for col in self.df_selected.columns if col.lower() in user_subjects]
            print(matching_columns)

            if len(matching_columns) != len(user_subjects):
                # prompts user to select subject(s) again if selected subjects do not match column names
                print("The selected subjects don't match with the column names of the dataframe.")
                user_subjects = input("Please select again\n").lower()
                user_subjects = re.split(r'[,\s;|]+', user_subjects)
            else:
                wrong_input = False

        return matching_columns

    def display_time_range(self):
        date_range = (self.df_selected['DateTime'].min(), self.df_selected['DateTime'].max())
        print("DateTime range:", date_range)

    def select_time_range(self, selected_subset):
        out_of_range = True
        while out_of_range:
            # prompts the user to select a time period within the DateTime range
            user_start = pd.to_datetime(input("Please select a starting time period within the DateTime range\n"))
            user_end = pd.to_datetime(input("Please select an ending time period within the DateTime range\n"))

            min = pd.to_datetime(self.df_selected['DateTime'].min())
            max = pd.to_datetime(self.df_selected['DateTime'].max())

            # checks if the selected time range is valid
            if (user_start >= min) & (user_end >= user_start) & (user_end <= max):
                out_of_range = False
            else:
                print("Selected time period is false or outside the DateTime range.")
                print("Min DateTime", min)
                print("Max DateTime", max)

        # filters rows based on user's time period selection
        filtered_subset = selected_subset[(pd.to_datetime(selected_subset['DateTime']) >= user_start) &
                               (pd.to_datetime(selected_subset['DateTime']) <= user_end)]

        return filtered_subset



if __name__ == "__main__":
    select_data = DataSelection()
    select_data.select_data()
    select_data.save_selected_data()
    print("Data Selection is Saved!")




