
#List
#List are a collection data structure / array kid of data structure in Python
#Unlike other collection or array, List are not homogenous, means List can hold any kind of data type
#List are mutable. Means, values within the list can be modified.

#https://www.geeksforgeeks.org/python-list/

print('List')
print('*'*5)
l = []
print(l)
l.append(10)
l.append('Sree')
l.append(list('Chars'))
print(l)

# Lists are mutable, and hence, they can be altered even after their creation.
#List in Python are ordered and have a definite count. The elements in a list are indexed according to a
# definite sequence and the indexing of a list is done with 0 being the first index.
#  Unlike Sets, list may contain mutable elements. # unlike set, list allow duplicate values
# use append method to add item to the end of the list
# extend method take a collection of items to be added to the list. insted of using multiple append, you can use extend to attach multiple items.
# use insert(position,item) use insert method to insert am item into the List at  desired position. Item in the desired position will be pushed to next index.


some_list = [10,3,1,13]
print(some_list)

#multi-dimensional list
some_list =[[10,3,1,13],[4,4],['s','n','c']]
print(some_list)
some_list.append('LAST ITEM')
print(some_list)
some_list.extend(a for a in 'SREEJITH')
some_list.insert(len(some_list)-1,'INS')
print(some_list)



# Accessing elements in list

list_single = ['Indian','Indi','India']
list_multiple = [['Indian','Indi','India'],['Indi_1','India_2'],['Indian']]
list_nested = [1,2,[3,4,5,[6,7,8]]]
print(list_single[0])
print(list_multiple[1][1])
print(list_nested[2][3][2]) # return 8

#slicing
new_list=list_single[1:3]
print(new_list)
new_list=list_single[-1]
print(new_list)

# Elements can be removed from the List by using built-in remove() function but an Error arises if element doesn’t exist in the set.
# Remove() method only removes one element at a time, to remove range of elements, iterator is used. The remove() method removes the specified item.
# Note – Remove method in List will only remove the first occurrence of the searched element

# Creating a List 
List = [1, 2, 3, 4, 5, 5,  
        6, 6, 6, 5, 5, 12] 
print("Intial List: ") 
print(List) 
  
# Removing elements from List 
# using Remove() method -> remove the first occupance of element
List.remove(5) 
List.remove(6) 
print("\nList after Removal of two elements: ") 
print(List) 

#remove all occurance of a specific element
List = list(filter(lambda a: a!=5, List))
print(List) 

print([x for x in List if x!=6])

