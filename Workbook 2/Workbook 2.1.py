# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:23:35 2019

@author: brand
"""

#Workbook 2.1
#Page 13 & 14

#folder: C:/Users/brand/OneDrive/Documents/datasets/weekly_call_data

import pandas as pd
import glob

filenames = glob.glob(r'C:/Users/brand/OneDrive/Documents/datasets/weekly_call_data/*.xlsx')
all_data = pd.DataFrame()
for f in filenames:
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
print(all_data.describe())