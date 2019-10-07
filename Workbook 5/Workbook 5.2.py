#pg 57
#10/7/2019

import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]

dataset = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data = dataset,
                  columns=['Names','Grades','BS Degrees','MS Degrees','PhD Degrees'])

#This is how we can save code and get all of the summary stats. 
print(df.describe())
#printing median of all values
print(df.median())
#printing the most often values
print(df.mode())
#getting the variance of the data
print(df.var())
#Printing correlation between data 
print(df.corr())