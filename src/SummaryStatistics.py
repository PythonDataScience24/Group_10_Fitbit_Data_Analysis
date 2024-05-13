import pandas as pd
import numpy as np

"""
    An instance of this class is able to generate (some) custom statistics.
"""
class SummaryStatistics:

    def __init__(self):
        self.df = pd.read_csv("../preprocessed_data/minutes.csv")

    """
    Calculates the average of a variable in a given timestep, e.g. Calories per Day
    per Id
    
    @:param var: string of the columnname of the df, the variable of which the mean is to be calculated
    @:param timestep: Element of {"Month", "Day", "Hour"}, timestep of the mean 
    
    @:return dataframe of with the columns ["Id", Variable/Time]
    """
    def variable_per_time_df(self, var, timestep):
        if (timestep == "Day"):
            helparray = ["Id", "Month", "Day"]
        elif (timestep == "Hour"):
            helparray = ["Id", "Month", "Day", "Hour"]
        else:
            helparray = ["Id", "Month"]

        helparray2 = helparray.copy()
        helparray2.append(var)

        return self.df[helparray2].groupby(helparray).mean()


