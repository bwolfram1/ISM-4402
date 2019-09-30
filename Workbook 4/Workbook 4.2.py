# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:42:16 2019

@author: brand
"""
#importing the libraries and dataset 
import pandas as pd
import numpy as np
df = pd.read_csv('C:/Users/brand/OneDrive/Documents/ISM4402/datasets/gradedata.csv')
#creating a column based on a certain conditional using the where function from numpy
df['timemgmt'] = np.where((df['exercise']>3) & (df['hours'] > 17),'busy','')
#printing the result
print(df)