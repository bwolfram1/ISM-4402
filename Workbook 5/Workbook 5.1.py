#pg 53
#10/7/2019


import pandas as pd
import numpy as np
#importing the csv file 
df = pd.read_csv("C:/Users/brand/OneDrive/Documents/ISM4402/datasets/gradedata.csv")
print(df)
#getting 500 random samples
df500 = df.take(np.random.permutation(len(df))[:500])
print(df500)
