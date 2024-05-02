import pandas as pd


class MergeMinutes:
    """
        To Merge the data in the csv file into a single dataframe we do the following:
        1. For each Information Category (Calories, Intensities, METs, Sleep, Steps):
            a. Read the csv file into a dataframe
            b. Concat the two different timeframes into a single dataframe
            c. Convert the ActivityMinute to datetime
            d. Perform any additional operations on the dataframe
                - For Sleep, rename and drop columns
                - For Sleep, round down all the minutes to the nearest
                - For HeartRate, create a new dataframe with the mean of the heart rates for each minute and column ID, ActivityMinute, and HeartRate
                - For HeartRate, rename columns
        2. Merge all the dataframes into a single dataframe
        3. Add additional date columns (month, day, weekday and hour) to the dataframe for easier analysis
        3. Save the dataframe to a csv file
    """

    def __init__(self):
        self.df_minutes = None
        pass

    def merge_all_dataframes(self):
        print("Merging all dataframes...")

        # merge all data into one single dataframe
        self.df_minutes = pd.merge(self.minute_calories(), self.minute_intensities(), on=["Id", "ActivityMinute"],
                                   how="outer")
        self.df_minutes = pd.merge(self.df_minutes, self.minute_METs(), on=["Id", "ActivityMinute"], how="outer")
        self.df_minutes = pd.merge(self.df_minutes, self.minute_sleep(), on=["Id", "ActivityMinute"], how="outer")
        self.df_minutes = pd.merge(self.df_minutes, self.minute_steps(), on=["Id", "ActivityMinute"], how="outer")
        self.df_minutes = pd.merge(self.df_minutes, self.minute_heart_rate(), on=["Id", "ActivityMinute"], how="outer")

        self.df_minutes = self.df_minutes.rename(columns={"ActivityMinute": "DateTime"})

        # add additional date columns to the dataframe for easier analysis
        self.df_minutes['Month'] = self.df_minutes['DateTime'].dt.month
        self.df_minutes['Day'] = self.df_minutes['DateTime'].dt.day
        self.df_minutes['WeekDay'] = self.df_minutes['DateTime'].dt.weekday
        self.df_minutes['Hour'] = self.df_minutes['DateTime'].dt.hour

        self.df_minutes = self.df_minutes.set_index(["Id", "DateTime", "Month", "Day", "WeekDay", "Hour"])

    def save_merged_dataframe(self):
        """
        Save the merged dataframe to a CSV and pickle file.
        The pickle is a binary file that can be used to save the dataframe including indexes.
        """
        print("Saving merged dataframe to CSV and pickle...")
        self.df_minutes.to_csv("../preprocessed_data/minutes.csv")
        self.df_minutes.to_pickle("../preprocessed_data/minutes.pkl")

    def load_pickle_to_dataframe(self):
        """
        Save the merged dataframe to a CSV and pickle file.
        The pickle is a binary file that can be used to save the dataframe including indexes.
        """
        print("Load merged dataframe from pickle...")
        self.df_minutes = pd.read_pickle('../preprocessed_data/minutes.pkl')

    def minute_calories(self):
        """
        Read and process calories data in minute resolution.
        """
        print("Reading and processing minute calories data...")
        df_minute_calories = pd.concat(
            [pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/minuteCaloriesNarrow_merged.csv"),
             pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/minuteCaloriesNarrow_merged.csv")],
            ignore_index=True)
        df_minute_calories["ActivityMinute"] = pd.to_datetime(df_minute_calories["ActivityMinute"],
                                                              format="%m/%d/%Y %I:%M:%S %p")
        return df_minute_calories

    def minute_intensities(self):
        """
        Read and process the intensities data in minute resolution.
        """
        print("Reading and processing minute intensities data...")
        df_minute_intensities = pd.concat(
            [pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/minuteIntensitiesNarrow_merged.csv"),
             pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/minuteIntensitiesNarrow_merged.csv")],
            ignore_index=True)
        df_minute_intensities["ActivityMinute"] = pd.to_datetime(df_minute_intensities["ActivityMinute"],
                                                                 format="%m/%d/%Y %I:%M:%S %p")
        return df_minute_intensities

    def minute_METs(self):
        """
        Read and process METs (Metabolic equivalent of task) data in minute resolution.
        """
        print("Reading and processing minute METs data...")
        df_minuteMETs = pd.concat([pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/minuteMETsNarrow_merged.csv"),
                                   pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/minuteMETsNarrow_merged.csv")],
                                  ignore_index=True)
        df_minuteMETs["ActivityMinute"] = pd.to_datetime(df_minuteMETs["ActivityMinute"], format="%m/%d/%Y %I:%M:%S %p")
        return df_minuteMETs

    def minute_sleep(self):
        """
        Read and process the sleep data in minute resolution.
        """
        print("Reading and processing minute sleep data...")
        df_minute_sleeps = pd.concat([pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/minuteSleep_merged.csv"),
                                      pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/minuteSleep_merged.csv")],
                                     ignore_index=True)
        df_minute_sleeps = df_minute_sleeps.rename(columns={"date": "ActivityMinute"})

        df_minute_sleeps["ActivityMinute"] = pd.to_datetime(df_minute_sleeps["ActivityMinute"]).dt.floor("min")
        df_minute_sleeps["ActivityMinute"] = pd.to_datetime(df_minute_sleeps["ActivityMinute"])

        df_minute_sleeps = df_minute_sleeps.rename(columns={"value": "Sleep"})
        df_minute_sleeps = df_minute_sleeps.drop(columns=["logId"])
        return df_minute_sleeps

    def minute_steps(self):
        """
        Read and process steps data in minute resolution.
        :return:
        """
        print("Reading and processing minute steps data...")
        df_minute_steps = pd.concat([pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/minuteStepsNarrow_merged.csv"),
                                     pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/minuteStepsNarrow_merged.csv")],
                                    ignore_index=True)
        df_minute_steps["ActivityMinute"] = pd.to_datetime(df_minute_steps["ActivityMinute"],
                                                           format="%m/%d/%Y %I:%M:%S %p")
        return df_minute_steps

    def minute_heart_rate(self):
        """
        Read and process heart rates data in minute resolution. We need to grop the data by minute and
        take the mean of the heart rates since the data is in the seconds resolution.
        """
        print("Reading and processing second heart rates data...")
        df_seconds_heart_rates = pd.concat(
            [pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/heartrate_seconds_merged.csv"),
             pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/heartrate_seconds_merged.csv")],
            ignore_index=True)

        df_seconds_heart_rates["Time"] = pd.to_datetime(df_seconds_heart_rates["Time"], format="%m/%d/%Y %I:%M:%S %p")

        df_seconds_heart_rates.rename(columns={"Time": "ActivityMinute"}, inplace=True)
        df_minute_heart_rates = df_seconds_heart_rates.groupby(
            ["Id", pd.Grouper(key="ActivityMinute", freq="1min")]).mean()

        df_minute_heart_rates = df_minute_heart_rates.rename(columns={"Value": "Heartrate"})
        return df_minute_heart_rates


if __name__ == "__main__":
    merge_minutes = MergeMinutes()
    merge_minutes.merge_all_dataframes()
    merge_minutes.save_merged_dataframe()
    print("Merging Done!")
