#Tuples
# Tuples are sequence of immutable python objects, The difference of Tuple from List is that
# Tuples are immutable (value can not be changed once declared)
# The important difference between a list and a tuple is that tuples are immutable. Also, Tuples are hashable whereas lists are not.
# Faster then List

print('Tuples')
print('*'*6)
tup = (None)
print(tup.__hash__())
tup = (23,'Sreejith',('ne st ed'.split(' ')))
print(tup)


#Packing and unpacking tuples
#Packing where values are put into a Tuple
#Unpacking where values are extracted out from the tuple.
#When unpacking we must provide correct number of argument on where values will be place.
# If number of elements in tuple is not know then we can use **args to capture dynamic number of variables
print("\n\n\n")
print("Packing and unpacking tuples")
a = ('NIT', 5000, 'Engineering')
print(a)
#unplacking the values
(a1, a2, a3) = a
print(a1 +'\t'+ str(a2)+'\t'+a3 )
#In unpacking of tuple number of variables on left hand side should be equal to number of values in given tuple a.
#Python uses a special syntax to pass optional arguments (*args) for tuple unpacking. the type of *args is list, **kwarg is dictionary.
 

# here first and last element is unpacked into X and Y and rest of it assigned to *Z

tup = ('Sreejith',100,300,23.67,'Nair',20)

(x,*z,y) = tup

print(f'first value: {x} \nlast value:{y}\n rest of the values:{z}')
pack = (a1,a2,a3)
print(f'New pack:{pack}')
print("\n\n\n")

print('Python tuples can be unpacked using a function in function tuple is passed and in function values are unpacked into normal variable')

# Python code to study about 
# unpacking python tuple using function 
  
# function takes normal arguments 
# and multiply them 
def result(x, y, z): 
    return x * y * z
# function with normal variables 
print (result(10, 100, 0.5)) 
  
# A tuple is created 
z = (10, 100, 0.5) 
  
# Tuple is passed 
# function unpacked them 
  
print (result(*z)) 


def dynamic_parameter(*args): 
    for i in args:
        print (i)
# function with normal variables 
print (dynamic_parameter(10, 100, 0.5)) 
dynamic_parameter(10)

'''
Tuple is a collection of Python objects much like a list. The sequence of values stored in a tuple can be of any type,
and they are indexed by integers. The important difference between a list and a tuple is that tuples are immutable.
Also, Tuples are hashable whereas lists are not.

Values of a tuple are syntactically separated by ‘commas’. Although it is not necessary, 
it is more common to define a tuple by closing the sequence of values in parentheses.
'''
tup_a = 1, 2, 3, 'Sreejith'
print(type(tup_a))

"""
Tuples are immutable, and usually, they contain a sequence of heterogeneous elements that are
accessed via unpacking or indexing (or even by attribute in the case of named tuples)

In Python, tuples are created by placing sequence of values separated by ‘comma’ with or without
the use of parentheses for grouping of data sequence. Tuples can contain any number of elements and
 of any datatype (like strings, integers, list, etc.).

 Tuples can also be created with a single element, but it is a bit tricky. Having one element in the parentheses is not sufficient, there must be a trailing ‘comma’ to make it a tuple.
 Note – Creation of Python tuple without the use of parentheses is known as Tuple Packing.
"""

#create empty tuple

empty_tuple = ()
print(type(empty_tuple))

tuple_with_one_val = (21,) #if we don't put comma at the end the value will be considered as int 21

tuple_with_differ_types = ('string', 2, 00.22)
print(tuple_with_differ_types)

#converting set into a tuple instance
set_with_differ_types_cast = ['string', 2,0.91]
print(tuple(set_with_differ_types_cast))


#Create tuple with the help of for loop

v = tuple(i for i in range(1,6))
print(v)

#concatenation of tuples

t1 = tuple(i for i in range(1,6))
t2 = tuple( c for c in 'Sreejith')
t3 = t1+t2
print(t3)
t3 = t2+t1
print(t3)

#Slicing and reversing
#With a specific index you can get a value. But with slicing you can extract a set of value ( subset)

t1 = tuple(a for a in 'TheLoansEngine')
reverse = t1[::-1]
print(reverse)

middle= t1[3:8] # starting from index 3 (L) and slice up to index 8 (excluding the index) (s)
print(middle)

#deleting tuples.
#tuples are immutable. This means you can't delete one element in a tuple. rather we had to delete tuple itself

del(middle)
#print(middle) # this will throw error


#removing empty tuple from list of tuples ( SOLVING without any language support)
list_tuples=[('a'),(),(1,2,3)]
non_duplicate_tuples = []
i = 0
while len(list_tuples)>i:
    if list_tuples[i] is not tuple():
        non_duplicate_tuples.append(list_tuples[i])
    i+=1
del(list_tuples)
print(non_duplicate_tuples)

#alternately
list_tuples=[('a'),(),(1,2,3)]
non_duplicate_tuples=[t for t in list_tuples if t] #Solving with list compression
print(non_duplicate_tuples)

#alternately SOLVE using filter method
def remove_empty(tuples):
    tuples = filter(None,tuples)
    return tuples
list_tuples=[('a'),(),(1,2,3)]
print( set(remove_empty(list_tuples)))


#re-write own logic using filter
non_duplicate_tuples=[]
list_tuples=[('a'),(),(1,2,3)]
non_duplicate_tuples.append(a for a in filter(None,list_tuples))
print(non_duplicate_tuples)

#Compression
# return a set of doubled odd numbers
t_values = (1,2,34,5,6,7,8,19,17)
result = [v*v for v in t_values if v % 2 >= 1 ]
print(result)

def is_prime(n)->bool:
    '''
    This return a boolean based on whether or not the given number is prime
    '''
    if( n <= 2):
        return True

    for a in range(2,n-1):
        if n%a==0:
            return False
        else:
            continue
    return True

t_values = (1,2,34,5,6,7,8,19,17)
result = [v for v in t_values if is_prime(v) ]
print(result)