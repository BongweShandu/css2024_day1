# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:39 2024

@author: bongw
"""

"""
Storing data in Python
1. Lists
2. Dictionaries
3. Data Frames - specific to pandas
"""

import pandas
file = pandas.read_csv("country_data.csv")

print(file)

age1 = 30
age2 = 25
age3 = 29

# Lists - square brackes for variables in a list format
age = [30, 25, 29, 46, 22]

print(age)

# To access value (for example, age 0 due to indexing)
print(age[0])
print(age[2])

#To print the minimum
print(min(age))

#To print the sum
print(sum(age))

#To print the lenghth of the list
print(len(age))

#To print average
print(sum(age)/len(age))

"""



