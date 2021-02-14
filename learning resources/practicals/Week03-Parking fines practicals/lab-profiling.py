# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Project : acs-project-data_science      
@File    : lab-profiling.py
@Author  : Billy Sheng 
@Contact : shengdl999links@gmail.com  
@Date    : 2021/2/9 6:34 下午
@Version  : 1.0.0
@License : Apache License 2.0
@Desc    : None
"""

import pandas as pd

df = pd.read_csv('Quarter 4 201920.csv')

# print(df.head())

# print(df.shape)
# print(df.describe)
print(df.info())