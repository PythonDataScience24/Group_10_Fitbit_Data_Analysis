import pandas as pd

"""
    To Merge the data in the csv file into a single dataframe we do the following:
    1. For each Information Category (Calories, Intensities, METs, Sleep, Steps):
        a. Read the csv file into a dataframe
        b. Concat the two different timeframes into a single dataframe
        c. Convert the ActivityMinute to datetime
        d. Set the index to Id and ActivityMinute
        e. Perform any additional operations on the dataframe
            - For Sleep, rename and drop columns
            - For Sleep, round down all the minutes to the nearest
            - For HeartRate, create a new dataframe with the mean of the heart rates for each minute and column ID, ActivityMinute, and HeartRate
            - For HeartRate, rename columns
    2. Merge all the dataframes into a single dataframe
    3. Save the dataframe to a csv file
"""


df_minuteCalories = pd.concat([pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/minuteCaloriesNarrow_merged.csv"), pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/minuteCaloriesNarrow_merged.csv")], ignore_index=True)
df_minuteCalories["ActivityMinute"] = pd.to_datetime(df_minuteCalories["ActivityMinute"], format="%m/%d/%Y %I:%M:%S %p")
df_minuteCalories = df_minuteCalories.set_index(["Id", "ActivityMinute"])

df_minuteIntensities = pd.concat([pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/minuteIntensitiesNarrow_merged.csv"), pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/minuteIntensitiesNarrow_merged.csv")], ignore_index=True)
df_minuteIntensities["ActivityMinute"] = pd.to_datetime(df_minuteIntensities["ActivityMinute"], format="%m/%d/%Y %I:%M:%S %p")
df_minuteIntensities = df_minuteIntensities.set_index(["Id", "ActivityMinute"])

df_minuteMETs = pd.concat([pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/minuteMETsNarrow_merged.csv"), pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/minuteMETsNarrow_merged.csv")], ignore_index=True)
df_minuteMETs["ActivityMinute"] = pd.to_datetime(df_minuteMETs["ActivityMinute"], format="%m/%d/%Y %I:%M:%S %p")
df_minuteMETs = df_minuteMETs.set_index(["Id", "ActivityMinute"])

df_minuteSleeps = pd.concat([pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/minuteSleep_merged.csv"), pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/minuteSleep_merged.csv")], ignore_index=True)
df_minuteSleeps = df_minuteSleeps.rename(columns={"date": "ActivityMinute"})

df_minuteSleeps["ActivityMinute"] = pd.to_datetime(df_minuteSleeps["ActivityMinute"]).dt.floor("min")
df_minuteSleeps.head()
df_minuteSleeps["ActivityMinute"] = pd.to_datetime(df_minuteSleeps["ActivityMinute"])

df_minuteSleeps = df_minuteSleeps.rename(columns={"value": "Sleep"})
df_minuteSleeps = df_minuteSleeps.drop(columns=["logId"])
df_minuteSleeps = df_minuteSleeps.set_index(["Id", "ActivityMinute"])

df_minuteSteeps = pd.concat([pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/minuteStepsNarrow_merged.csv"), pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/minuteStepsNarrow_merged.csv")], ignore_index=True)
df_minuteSteeps["ActivityMinute"] = pd.to_datetime(df_minuteSteeps["ActivityMinute"], format="%m/%d/%Y %I:%M:%S %p")
df_minuteSteeps = df_minuteSteeps.set_index(["Id", "ActivityMinute"])

df_secondsHeartRates = pd.concat([pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/heartrate_seconds_merged.csv"), pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/heartrate_seconds_merged.csv")], ignore_index=True)
df_secondsHeartRates["Time"] = pd.to_datetime(df_secondsHeartRates["Time"], format="%m/%d/%Y %I:%M:%S %p")

df_secondsHeartRates.rename(columns={"Time": "ActivityMinute"}, inplace=True)
df_minuteHeartRates = df_secondsHeartRates.groupby(["Id", pd.Grouper(key="ActivityMinute", freq="1min")]).mean()
df_minuteHeartRates = df_minuteHeartRates.rename(columns={"Value": "Heartrate"})


df_minutes = pd.merge(df_minuteCalories, df_minuteIntensities, on=["Id", "ActivityMinute"], how="outer")
df_minutes = pd.merge(df_minutes, df_minuteMETs, on=["Id", "ActivityMinute"], how="outer")
df_minutes = pd.merge(df_minutes, df_minuteSleeps, on=["Id", "ActivityMinute"], how="outer")
df_minutes = pd.merge(df_minutes, df_minuteSteeps, on=["Id", "ActivityMinute"], how="outer")
df_minutes = pd.merge(df_minutes, df_minuteHeartRates, on=["Id", "ActivityMinute"], how="outer")

df_minutes.to_csv("../data/Custom_Dataframes/minutes.csv")