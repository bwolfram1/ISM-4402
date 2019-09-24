# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:09:32 2019

@author: brand
"""

#Ch3 page 25

import pandas as pd 
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,-2,77,78,101]
GradeList = zip(names,grades)

df = pd.DataFrame(data = GradeList,columns = ['Names','Grades'])
print(df)
#Limiting grade possibilies
df.loc[(df['Grades'] >= 100,'Grades')] = 100
df.loc[(df['Grades'] < 0,'Grades')] = 0


print(df)