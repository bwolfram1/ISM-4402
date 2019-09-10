# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:58:15 2019

@author: brand
"""


#Personal Income (Bureau of Economic Analysis) — NAICS
#Link: https://www2.census.gov/library/publications/2011/compendia/usa-counties/excel/PEN01.xls (warning it'll download the excel file upon loading)
import pandas as pd
df = pd.read_excel("PEN01.xls")
print(df.head())