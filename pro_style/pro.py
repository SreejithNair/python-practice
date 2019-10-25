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
