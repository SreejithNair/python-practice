
'''
The ChainMap class manages a sequence of dictionaries, and searches through them in the order they appear to find
values associated with keys. A ChainMap makes a good “context” container, since it can be treated as a stack for which
changes happen as the stack grows, with these changes being discarded again as the stack shrinks.
'''

import collections

a = {'a':'1','c':'1'}
b = {'b':'2','c':'2'}

m = collections.ChainMap(a,b)

print(m.maps)
print(list(m.keys()))
print(list(m.values()))



c = {'a':'3','b':'4'}
m=m.new_child(c)
'''
The child mappings are searched in the order they are passed to the constructor, so the value reported for the key 'c' comes from the a dictionary.
'''
print(m.maps)
print(list(m.keys()))
print(list(m.values()))

#reverse
m = reversed(m.maps)
print(m.maps)
print(list(m.keys()))
print(list(m.values()))

