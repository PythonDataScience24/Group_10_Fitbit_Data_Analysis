import pandas as pd
import os
#Merge Data of two timeperiods to one dataframe
#Dataframe is Multiindexed by Id and ActivityDate

df_DailyActivity312 = pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/dailyActivity_merged.csv")
df_DailyActivity412 = pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/dailyActivity_merged.csv")
df_DailyActivity = pd.concat([df_DailyActivity312,df_DailyActivity412], ignore_index=True)
df_DailyActivity = df_DailyActivity.set_index(["Id", "ActivityDate"])
df_DailyActivity.to_csv("../data/Custom_Dataframes/DailyActivity.csv")

#too large for github execute this locally
#df_heartrate_seconds312 = pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/heartrate_seconds_merged.csv")
#df_heartrate_seconds412 = pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/heartrate_seconds_merged.csv")
#df_heartrate_seconds = pd.concat([df_heartrate_seconds312,df_heartrate_seconds412],ignore_index=True)
#df_heartrate_seconds = df_heartrate_seconds.set_index(["Id", "Time"])
#df_heartrate_seconds.to_csv("../data/Custom_Dataframes/heartrate_seconds.csv")

df_hourlyCalories312 = pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/hourlyCalories_merged.csv")
df_hourlyCalories412 = pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/hourlyCalories_merged.csv")
df_hourlyCalories = pd.concat([df_hourlyCalories312,df_hourlyCalories412],ignore_index=True)
df_hourlyCalories = df_hourlyCalories.set_index(["Id", "ActivityHour"])
df_hourlyCalories.to_csv("../data/Custom_Dataframes/hourlyCalories.csv")

df_hourlyIntensities312 = pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/hourlyIntensities_merged.csv")
df_hourlyIntensities412 = pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/hourlyIntensities_merged.csv")
df_hourlyIntensities = pd.concat([df_hourlyIntensities312,df_hourlyIntensities412],ignore_index=True)
df_hourlyIntensities = df_hourlyIntensities.set_index(["Id", "ActivityHour"])
df_hourlyIntensities.to_csv("../data/Custom_Dataframes/hourlyIntensities.csv")

df_hourlySteps312 = pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/hourlySteps_merged.csv")
df_hourlySteps412 = pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/hourlySteps_merged.csv")
df_hourlySteps = pd.concat([df_hourlySteps312,df_hourlySteps412],ignore_index=True)
df_hourlySteps = df_hourlySteps.set_index(["Id", "ActivityHour"])
df_hourlySteps.to_csv("../data/Custom_Dataframes/hourlySteps.csv")

df_minuteSleep312 = pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/minuteSleep_merged.csv")
df_minuteSleep412 = pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/minuteSleep_merged.csv")
df_minuteSleep = pd.concat([df_minuteSleep312,df_minuteSleep412],ignore_index=True)
df_minuteSleep = df_minuteSleep.set_index(["Id", "date"])
df_minuteSleep.to_csv("../data/Custom_Dataframes/minuteSleep.csv")

df_weightLogInfo312 = pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/weightLogInfo_merged.csv")
df_weightLogInfo412 = pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/weightLogInfo_merged.csv")
df_weightLogInfo = pd.concat([df_weightLogInfo312,df_weightLogInfo412],ignore_index=True)
df_weightLogInfo = df_weightLogInfo.set_index(["Id", "Date"])
df_weightLogInfo.to_csv("../data/Custom_Dataframes/weightLogInfo.csv")

