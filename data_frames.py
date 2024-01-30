# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:31:29 2024

@author: bongw
"""

"""
"Data frames"
"""

fruits = ["apple", "banana","orange","grape","kiwi"]
Size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]
fruit_sizes = {
                'fruits': fruits,
                'sizes': Size_nm}


#df = data frame

import pandas as pd
df = pd.DataFrame(fruit_sizes)

print(df['fruits'])
print(df['sizes'])
print(df['sizes'].min)
print(df['sizes'].mean)
print(df.describe())
print(df[df["sizes"]>10])

print(df[1:3])

#To add new column data
prices = [10.00, 12.50, 16.00, 23.00, 7.00]
df['prices'] = prices
df.drop(columns = ["sizes"], inplace = True)
