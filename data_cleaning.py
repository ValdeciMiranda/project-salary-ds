# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 15:17:24 2023

@author: Valde
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs_final.csv')

#Salary parsing

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K', '').replace('$', ''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))

df['min_salary'] = min_hr.apply(lambda x: int(float(x.split('-')[0])))
df['max_salary'] = min_hr.apply(lambda x: int(float(x.split('-')[-1])))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#Company name text only

df['company_txt'] = df.apply(lambda x: x['Company Name'][:-3] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

#state field

df['job_state'] = df['Location'].apply(lambda x: str(x).split(',')[-1])
df.job_state.value_counts()

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#age of company

#df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x) Founded not disponible (all are -1)

#parsing of job description (python, etc.)

df['Job Description'][0]

#Most usable tools for data science

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

#r studio
df['r_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)

#spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df.to_csv('salary_data_cleaned.csv', index = False)

pd.read_csv('salary_data_cleaned.csv')
