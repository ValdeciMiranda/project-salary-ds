# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 15:14:21 2023

@author: Valde
"""
import pandas as pd

#Concatenate all CSVs of all jobs

df1 = pd.read_csv('glassdoor_jobs_1.csv')
df2 = pd.read_csv('glassdoor_jobs_2.csv')
df3 = pd.read_csv('glassdoor_jobs_3.csv')
df4 = pd.read_csv('glassdoor_jobs_4.csv')
df5 = pd.read_csv('glassdoor_jobs_5.csv')
df6 = pd.read_csv('glassdoor_jobs_6.csv')
df7 = pd.read_csv('glassdoor_jobs_7.csv')
df8 = pd.read_csv('glassdoor_jobs_8.csv')
df9 = pd.read_csv('glassdoor_jobs_9.csv')
df10 = pd.read_csv('glassdoor_jobs_10.csv')
df11 = pd.read_csv('glassdoor_jobs_11.csv')

final_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11])

final_df.to_csv('glassdoor_jobs_final.csv', index = False)