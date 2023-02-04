# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 13:31:35 2023

@author: Valde
"""

import my_glassdoor_web_scraper as gs
import pandas as pd

path = r"C:/Program Files (x86)/chromedriver.exe"

df = gs.get_jobs('data scientist', 100, path, 15)

df.to_csv('glassdoor_jobs_11.csv', index = False)