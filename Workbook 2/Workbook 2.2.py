# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:48:37 2019

@author: brand
"""

#file:///C:/Users/brand/OneDrive/Documents/datasets/salesdata.db

import pandas as pd
from sqlalchemy import create_engine

df_file = r'C:/Users/brand/OneDrive/Documents/datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}".format(df_file))
#sql = 'SELECT name from sqlite_master'
sql = 'SELECT * FROM scores' 
sales_data_df = pd.read_sql(sql,engine)
print(sales_data_df)

