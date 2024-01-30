# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:18:20 2024

@author: bongw
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)
 
print(file.info())

print(file.describe())

file = pandas.read_csv("diab_data.csv")

print(file)

print(file.describe())

print(file.info())