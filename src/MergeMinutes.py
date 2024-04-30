import pandas as pd

"""
    To Merge the data in the csv file into a single dataframe we do the following:
    1. For each Information Category (Calories, Intensities, METs, Sleep, Steps):
        a. Read the csv file into a dataframe
        b. Concat the two different timeframes into a single dataframe
        c. Convert the ActivityMinute to datetime
        d. Set the index to Id and ActivityMinute
        (e). Rename the columns, drop columns, and round down the minutes to the nearest (only necceassary for Sleep)
    2. Merge all the dataframes into a single dataframe
    3. Save the dataframe to a csv file
"""

df_minuteCalories = pd.concat([pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/minuteCaloriesNarrow_merged.csv"), pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/minuteCaloriesNarrow_merged.csv")], ignore_index=True)
#convert ActivityMinute to datetime using the following format 3/12/2016 12:00:00 AM
df_minuteCalories["ActivityMinute"] = pd.to_datetime(df_minuteCalories["ActivityMinute"], format="%m/%d/%Y %I:%M:%S %p")
df_minuteCalories = df_minuteCalories.set_index(["Id", "ActivityMinute"])

df_minuteIntensities = pd.concat([pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/minuteIntensitiesNarrow_merged.csv"), pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/minuteIntensitiesNarrow_merged.csv")], ignore_index=True)
#convert ActivityMinute to datetime
df_minuteIntensities["ActivityMinute"] = pd.to_datetime(df_minuteIntensities["ActivityMinute"], format="%m/%d/%Y %I:%M:%S %p")
df_minuteIntensities = df_minuteIntensities.set_index(["Id", "ActivityMinute"])

df_minuteMETs = pd.concat([pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/minuteMETsNarrow_merged.csv"), pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/minuteMETsNarrow_merged.csv")], ignore_index=True)
#convert ActivityMinute to datetime
df_minuteMETs["ActivityMinute"] = pd.to_datetime(df_minuteMETs["ActivityMinute"], format="%m/%d/%Y %I:%M:%S %p")
df_minuteMETs = df_minuteMETs.set_index(["Id", "ActivityMinute"])

df_minuteSleeps = pd.concat([pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/minuteSleep_merged.csv"), pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/minuteSleep_merged.csv")], ignore_index=True)
#rename column date to ActivityMinute
df_minuteSleeps = df_minuteSleeps.rename(columns={"date": "ActivityMinute"})
#round down all the minutes to the nearest
df_minuteSleeps["ActivityMinute"] = pd.to_datetime(df_minuteSleeps["ActivityMinute"]).dt.floor("min")
df_minuteSleeps.head()
df_minuteSleeps["ActivityMinute"] = pd.to_datetime(df_minuteSleeps["ActivityMinute"])
#get datatype of ActivityMinute

#rename value to Sleep
df_minuteSleeps = df_minuteSleeps.rename(columns={"value": "Sleep"})
#remove column logId
df_minuteSleeps = df_minuteSleeps.drop(columns=["logId"])
df_minuteSleeps = df_minuteSleeps.set_index(["Id", "ActivityMinute"])

df_minuteSteeps = pd.concat([pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/minuteStepsNarrow_merged.csv"), pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/minuteStepsNarrow_merged.csv")], ignore_index=True)
#convert ActivityMinute to datetime
df_minuteSteeps["ActivityMinute"] = pd.to_datetime(df_minuteSteeps["ActivityMinute"], format="%m/%d/%Y %I:%M:%S %p")
df_minuteSteeps = df_minuteSteeps.set_index(["Id", "ActivityMinute"])

df_minutes = pd.merge(df_minuteCalories, df_minuteIntensities, on=["Id", "ActivityMinute"], how="outer")
df_minutes = pd.merge(df_minutes, df_minuteMETs, on=["Id", "ActivityMinute"], how="outer")
df_minutes = pd.merge(df_minutes, df_minuteSleeps, on=["Id", "ActivityMinute"], how="outer")
df_minutes = pd.merge(df_minutes, df_minuteSteeps, on=["Id", "ActivityMinute"], how="outer")

df_minutes.to_csv("../data/Custom_Dataframes/minutes.csv")