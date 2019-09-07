"""
Created on Fri Sep  6 23:44:06 2019

@author: bwolfram1
"""

import pandas as pd           #import the pandas library
file = "all_050_in_12.P1.csv" #defining the file name to be imported/read
df = pd.read_csv(file)        #importing the file as a dataframe
print(df.head())              #printing the first 5 rows of the dataframe to make sure we imported it right.
