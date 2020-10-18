from matplotlib import pyplot as plt
import pandas as pd
import csv

myDict = {}

with open('alabamaCovid19Data_10_13_2020.csv') as csv_file:
    dataFrame = pd.read_csv(csv_file) # makes a dataframe 
    col_names = list(dataFrame.columns.values) # gets the column names
    myDict = {col: list(dataFrame.loc[: , col]) for col in col_names} # .loc gets the row or col by name not index
    print(myDict)

    
#plt.plot()
#plt.show()