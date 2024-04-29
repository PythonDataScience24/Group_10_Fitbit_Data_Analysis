import pandas as pd
import numpy as np

df_DailyActivity312 = pd.read_csv("../data/Fitabase Data 3.12.16-4.11.16/dailyActivity_merged.csv")
df_DailyActivity412 = pd.read_csv("../data/Fitabase Data 4.12.16-5.12.16/dailyActivity_merged.csv")

df_DailyActivity = pd.merge(df_DailyActivity312,df_DailyActivity412)

#df_DailyActivity312 = df_DailyActivity312.set_index(["Id", "ActivityDate"])
#df_DailyActivity412 = df_DailyActivity412.set_index(["Id", "ActivityDate"])

df_DailyActivity.to_csv("../data/Custom Dataframes/DailyActivity.csv")
