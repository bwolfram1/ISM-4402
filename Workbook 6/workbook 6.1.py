# pg 60 and pg 63

import pandas as pd
df = pd.read_csv('C:/Users/brand/OneDrive/Documents/ISM4402/datasets/gradedata.csv')
print(df.head())
df = df.sort_values(by = ['fname','age','grade'])
print(df.head())