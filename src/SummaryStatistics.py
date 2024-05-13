import pandas as pd
import numpy as np


class SummaryStatistics:

    def __init__(self):
        self.df = pd.read_csv("../preprocessed_data/minutes.csv")

    def variable_per_time_df(self, var, timestep):
        if (timestep == "day"):
            helparray = ["Id", "Month", "Day"]
        elif (timestep == "hour"):
            helparray = ["Id", "Month", "Day", "Hour"]
        else:
            helparray = ["Id", "Month"]

        helparray2 = helparray.copy()
        helparray2.append(var)

        return self.df[helparray2].groupby(helparray).mean()


