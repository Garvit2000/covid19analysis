import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

data = read_csv("file.csv")  #to read a csv file containing covid data

#or we can directly fetch data from world bank api

data.head()
data.columns
data.describe()

sb.replot(x="total_cases", y="recovered", data = data)    #here we can insert requires variable against x or y axis to get a plot

sb.replot(x="total_cases", y="recovered",kind = "line", data = data)
