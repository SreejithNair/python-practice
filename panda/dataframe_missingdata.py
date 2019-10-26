#Checking for missing values using isnull() and notnull()
# importing pandas as pd
import pandas as pd
 
# importing numpy as np
import numpy as np
 
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
 
# creating a dataframe from list
df = pd.DataFrame(dict)
 
# using isnull() function  - return Trus if data is missing 
df.isnull()
print(df)
print(df.isnull())

'''
Filling missing values using fillna(), replace() and interpolate() :
In order to fill null values in a datasets, we use fillna(), replace() and interpolate() 
function these function replace NaN values with some value of their own.
All these function help in filling a null values in datasets of a DataFrame.
Interpolate() function is basically used to fill NA values in the dataframe but
it uses various interpolation technique to fill the missing values rather than hard-coding the value.
'''

df = df.fillna(0) # missing values will be replaced by 0

print(df)

'''
Dropping missing values using dropna() :
In order to drop a null values from a dataframe, we used dropna() 
function this fuction drop Rows/Columns of datasets with Null values in different ways.
'''
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
 
# creating a dataframe from list
df = pd.DataFrame(dict)
df = df.dropna()
print(df)
