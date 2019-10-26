import pandas as pd
import os as path

dir_path = path.getcwd()

'''
Indexing in pandas means simply selecting particular rows and columns of data from a DataFrame.
Indexing could mean selecting all the rows and some of the columns, some of the rows and all of the columns,
or some of each of the rows and columns. Indexing can also be known as Subset Selection.

Indexing a Dataframe using indexing operator []
'''
df = pd.read_csv(dir_path+'\\panda\\nba.csv',index_col='Name')
print(df)
first = df['Age']
print(first)

'''
Selecting values of a single row by Index_col
Indexing a DataFrame using .loc[ ] :
This function selects data by the label of the rows and columns. 
The df.loc indexer selects data in a different way than just the indexing operator. I
t can select subsets of rows or columns. It can also simultaneously select subsets of rows and columns.
'''
# retrieving row by loc method
first = df.loc["Avery Bradley"]
print(first)

'''
selecting row by index
Indexing a DataFrame using .iloc[ ] :
This function allows us to retrieve rows and columns by position. In order to do that, 
we’ll need to specify the positions of the rows that we want, and the positions of the columns 
that we want as well. The df.iloc indexer is very similar to df.loc but only uses integer locations to make its selections.
'''
first = df.iloc[4]
print(first)



'''
Iterating over rows :
In order to iterate over rows, we can use three function iteritems(), iterrows(), itertuples() . These three function will help in iteration over rows.
'''
# dictionary of lists
dic = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
# creating a dataframe from a dictionary 
df = pd.DataFrame(dic)
print(df)
for i, j in df.iterrows():
    print(i,j)

'''
Iterating over Columns :
In order to iterate over columns, we need to create a list of dataframe columns and then iterating through that list to pull out the dataframe columns.
'''

# creating a list of dataframe columns
columns = list(df)
 
for i in columns: 
    print (df[i])


for i in columns: 
    # printing the third element of the column
    print (df[i][2])

    '''
    Column Addition:
In Order to add a column in Pandas DataFrame, we can declare a new list as a column and add to a existing Dataframe.
    '''
    dic = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
# creating a dataframe from a dictionary 
df = pd.DataFrame(dic)
address = ['Kerala','Delhi','Chennai','Patna']
df["Address"]=address
print(df)

'''
Column Deletion:
In Order to delete a column in Pandas DataFrame, we can use the drop() method.
Columns is deleted by dropping columns with column names.
'''
#since axis was set equal to 1 and the changes were made in the original data frame since inplace was True.
df.drop('degree',axis=1,inplace=True)
print(df)

'''
Deleting rows
In Order to delete a row in Pandas DataFrame, we can use the drop() method. Rows is deleted by dropping Rows by index label.

by default drop() doesn’t modify the existing DataFrame, 
instead it returns a new dataframe. If we want to update the existing DataFrame in place then we need to pass another attribute i.e. inplace=True
'''
df.drop(1,inplace=True) # drop by row index
print(df)


'''
Define index and column names
'''
students = [ ('jack', 34, 'Sydeny' , 'Australia') ,
             ('Riti', 30, 'Delhi' , 'India' ) ,
             ('Vikas', 31, 'Mumbai' , 'India' ) ,
             ('Neelu', 32, 'Bangalore' , 'India' ) ,
             ('John', 16, 'New York' , 'US') ,
             ('Mike', 17, 'las vegas' , 'US')  ]
 
 
#Create a DataFrame object
dfObj = pd.DataFrame(students, columns = ['Name' , 'Age', 'City' , 'Country'], index=['a', 'b', 'c' , 'd' , 'e' , 'f']) 
print(dfObj)
#delete rows at modDfObj = dfObj.drop(['a' , 'b'])

#Delete a single Row in DataFrame by Row Index Label
modDfObj = dfObj.drop('b')

#Delete Multiple Rows in DataFrame by Index Labels
modDfObj = dfObj.drop(['a' , 'b'])

#Delete a Multiple Rows by Index Position in DataFrame
'''
As df.drop() function accepts only list of index label names only, so to delete the rows by position we need to create a list of index names from positions and then pass it to drop().
Suppose we want to delete the first two rows i.e. rows at index position 0 & 1 from the above dataframe object. Let’s see how to do that,
'''

modDfObj = dfObj.drop([dfObj.index[0] , dfObj.index[1]])