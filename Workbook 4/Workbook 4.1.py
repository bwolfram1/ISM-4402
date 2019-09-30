# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:57:15 2019

@author: brand
"""
#importing the libraries and dataset 
import pandas as pd
import numpy as np
df = pd.read_csv('C:/Users/brand/OneDrive/Documents/ISM4402/datasets/gradedata.csv')
#creating a column based on a certain conditional using the where function from numpy
df['gClass'] = np.where(df['grade']>=80,'pass','fail')
#printing the result
print(df.head())