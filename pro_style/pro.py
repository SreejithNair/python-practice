import functools as reduce


#List compression
l1 = [1,2,3]
l2 = [10,9,8]
even_from_l1 = [a for a in l1 if a%2==0]
print(even_from_l1)
even_from_l2 = [b for b in l2 if b%2==0]
print(even_from_l2)
result = [(a,b) for a in even_from_l1 for b in even_from_l2]
print(result)


#enumeration
def fn(v):
    return v*v

def modify_list(lst, fn):
    for i, v in enumerate(lst):
        lst[i] = fn(v)
    return lst

lst = [10, 20, 30]

new_list = modify_list(lst, fn)

print(new_list)


#python lamda
#Python lambda is a alternative approach to define a function.
#lambda arguments: expression
#lambda function can accept one or more argument but only one expression.
#The return value of the lambda function is the value that this expression is evaluated to.
# The use case of lambda over other standard function is when we need one of function or anonymous function or inline function
#Python lambda functions accept only one and only one expression.
#If your function has multiple expressions/statements, you are better off defining a function the traditional way instead of using lambdas.

f = lambda a,b: a+b #take two parameter and return sum of those
print(type(f))
print(id(f))
print(f(10,20))


#Using lambdas with map
# Map is a Python built-in function that takes in a function and a sequence as arguments and
# then calls the input function on each item of the sequence.

raw_lst = [ 10, 20, 30]
for m in map(lambda x: x**2,raw_lst):
    print(m)

#Using lambdas with filter
raw_lst = [ 17, 20, 30]
res = [a for a in filter(lambda a: a%2==0,raw_lst)] # list comprehension with higher order function filter
print(res)

#conditional list comprehension
#remove all occurance of a specific element
raw_lst = [ 10, 20, 30]
List = list(filter(lambda a: a!=5, raw_lst)) # higher order function filter
print(List) 
print([x for x in List if x!=6]) #conditional list comprehension

# list comprehension with conditional
num_list = [y for y in range(100) if y%2==0 and y%5==0]   #both mod 2 ==0 and mod 5 ==0
num_list = [y for y in range(100) if y%2==0 if y%5==0]   #This and above lines are same
print(num_list)

#if ..else with list comprehension
num_list = [f'{y} is Even' if y%2==0 else f'{y} is Odd' for y in range(20)]
print(num_list)

# nested list in list comprehension
# Transpose of a matrix A ( denoted by A to the power of T) - interchanging rows and columns  [1,2]  will be come [1, 3]
                                                                                            # [3,4]               [2, 4]
# in typical case we would do transpose of the matrix as below
matrix = [[1,2],[3,4]]
print(matrix)
re=[]
c_length=len(matrix[0])
for a in range(c_length):
    l=[]
    for b in range(c_length):
        l.append(matrix[b][a])
    re.append(l)
print(re)

#the above traditional logic can be writtern using nested iteration inside list comprehension
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)

# traditional and equivalent nested list comprehension


x1=[]
for i in range(2):
    for j in range(2):
        x1.append([i,j])
print(x1)

x = [[i,j] for i in range(2) for j in range(2)]
print(x)

matrix = [j for j in range(2)]
print(matrix) 

matrix = [j for j in range(2) for i in range(2)]
print(matrix) 

matrix = [[j for j in range(2)] for i in range(2)]
print(matrix) 


# map and filters are covered earlier.
# following demonstrate reduce function

print(reduce.reduce(lambda x,y: x*y,range(1,6))) #120 . one-liner code puzzle, we combined the two (integer) values by multiplying them (and the result was the factorial function).

#The reduce function iteratively combines two values from an iterable as specified in the first functional argument.
# In our case, the functional argument is an anonymous (lambda) function that takes two values x and y, combines them, and returns the result.

print(reduce.reduce(lambda x, y: x + [[z for z in range(y)]] , [1, 2, 3, 4], [ ])) 
#But in this puzzle, our two values x and y have a different data type. 
# The third argument of the reduce function specifies the initial value of x. You can see that the initial value of x is an empty list.

'''
However, value y still takes on each integer value of the list to be reduced (i.e., the second argument of the reduce function). So, we have y=1, y=2, y=3, and y=4.
Now, we repeatedly merge value y into the list x. Basically, we create a new list using list comprehension. The new list consists of all integer values up to y (exclusive).
This new list is then added to the old list (which was initially empty and is growing steadily).
Here is the exact procedure for each integer y in the list to be reduced:
(the right-hand side shows you how the new list is merged into the old list in each reduce step.)
y=1: [] + [[0]] = [[0]]
y=2: [[0]] + [[0,1]] = [[0], [0,1]]
y=3: [[0], [0,1]] + [[0,1,2]] = [[0], [0,1], [0,1,2]] 
y=4: [[0], [0,1], [0,1,2]] + [[0,1,2,3]] = [[0], [0,1], [0,1,2], [0,1,2,3]]

'''
print(reduce.reduce(lambda x, y: x + [[z for z in range(y)]] , [1, 2, 3, 4], [ ])) 


#do it your self
print(reduce.reduce(lambda x,y: x|{y}, [1, 1, 1, 1, 2, 3, 4], {0}))  #{0, 1, 2, 3, 4}
# {0}|{1}
# {0}|{1}|{1}}
# {0}|{1}|{1}}|{1}
# {0}|{1}|{1}}|{1}|{1}
x = {0}|{1}|{1}|{1}|{1}|{2}
print(x)
