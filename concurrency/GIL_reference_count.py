#Global Interpreter Lock (GIL) -> mutex/lock that allow one thread to hold control of the python interpreter
#This means that only one thread can be in a state of execution at any point in time. Because of this GIL, it can be a 
#performance bottleneck in CPU-bound and multi-threaded code.
#GIL allow only one thread to execute at any given point in time even in a multi-threaded architecture with more than one CPU core.

#Python uses reference counting for memory management. Objects created in python have a reference count variable that keep trace of the number
# of references that point to the object. In the following [] list has 3 references count a, b and the getrefcount(a)

import sys
a = []
b = a
print(f'ref count (a):{sys.getrefcount(a)}')
a = {}
del b
print(f'ref count (a):{sys.getrefcount(a)}')

#print(f'ref count (b):{sys.getrefcount(b)}') #will throw exception because the b is been deleted


# Back to scope of GIL in memory management

# In order for the correct memory management, these reference count variable needed protection from race conditions where two thread increase/decreases
# new instances through object allocation / object deletion. If this happen, it can cause either leaked memory that is never released or,
# even worst, incorrectly releases the memory while a reference to that object still exists.

#The reference count variable can be kept safe by adding locks to all data
# structures (objects) that are shared across threads so that they are not modified inconsistently. But adding locks like these to each object cause to exist
#multiple locking object for each data structure. This can cause to another issue of dead lock since objects might need to work together to achieve
#any given common goal. Or decreased performance due to repeated lock acquisition and release.

#GIL is a single lock on he interpreter itself which adds a rule that execution of any python bytecode requiring the interpreter lock.


#https://realpython.com/python-gil/