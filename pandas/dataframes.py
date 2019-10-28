import pandas as pd
import os as path

lst = ['Name','Age',[1,2,3]]
data = pd.DataFrame(lst)
print(data)
print('\n\n')
dic = {"Name":['Sreejith','Anay','Niya'],"Age":[37,5,11]}
data = pd.DataFrame(dic)
print(data)
print('\n\n')
data = {'Name':['Jai','Anuj','Sree'],
'Age':[27,24,34],
'Address':['Delhi','Kanpur','Kerala'],
'Qualification':['Msc','Ma','Mca']}

df = pd.DataFrame(data)
print(df)
print('\n\n')
print(df[['Name','Age']])
print('\n\n')

dir_path = path.getcwd()
print('Current working directory:',dir_path)

#making data frame though a csv file
df = pd.read_csv(dir_path+'\\panda\\nba.csv',index_col='Name')
print(df)
# retrieving row by loc method
first = df.loc["Avery Bradley"]
second = df.loc['R.J. Hunter']
print(first, '\n\n\n',second)

#access a specific data from the row
print(first.Age)
#update age of selected record
first.Age=31 # This will only update value in current instance and not permanant- A value is trying to be set on a copy of a slice from a DataFrame
print(first, '\n\n\n',second)


