#demo sequence list, tuple and range

#empty range
print("Working with range")
empty_range = range(0)
print(empty_range)

for v in range(1,5,1):
    print(v)

print("end")

#List
print("Working with list")

empty_list = []
print(empty_list)

new_list = list(range(1,5,1))
print(new_list)

#repeat same list 3 time in new list
new_list = new_list * 3
print(new_list)

#slice and return element starting from index 4 and before 7
sli_list = new_list[4:7]
print(f'sli_list: {sli_list}')

#slice s[i:j:k]
second_sliced_list = new_list[4:7:2]
print(f'second_sliced_list: {second_sliced_list}')

#slice from start to end index and skip 3 elememts before considering the result.
#input list : [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
#answer: [1, 4, 3, 2]
third_sliced_list = new_list[::3]

print(f'third_sliced_list - Length: {third_sliced_list}')

print(f'third_sliced_list: {len(third_sliced_list)}')

print(f'third_sliced_list - Min: {min(third_sliced_list)}')

print(f'third_sliced_list - Max: {max(third_sliced_list)}')

print(f'new_list : {new_list}')

print(f'count of 4 in  new_list: {new_list.count(4)}')

print(f'count of 10 in  new_list: {new_list.count(10)}')

print(f'index of first occurrence of 3 (at or after index 5 and before index 10): {new_list.index(4,5,10)}')


print('\n\n\n')

print(f'Itenms in sequence are copied by reference')

new_seq = [[1,2,3,4]] * 3
print(new_seq)
new_seq[0].append(10)
print(new_seq)


lists = [[]] * 3
print(lists)
lists[0].append(3)
print(lists)

print(f'Create a list of list')

new_list = [ [] for i in range(3)]
print(new_list)
new_list[0].append([1,5,1])
new_list[1].append([6,10])

print(new_list)


print('fDelete list items')

s = [10,3,4,23]
print(s)
s= []
print(s)

s_del = [10,3,4,23]
print(s_del)
del s_del[:]
print(s_del)

print(f'remove and retrive items (pop)')

s_led_2= [33,234,876,3,32]
s_led_2.pop(1)
print(s_led_2)
s_led_2.remove(33)
print(s_led_2)
s_led_2.pop(1)
print(s_led_2)


s_led_3= [33,234,1,876,3,32]
print(s_led_3)

print(s_led_3.reverse())


print('all about tuples')

new_tu = ()
print(f'empty tuples:{new_tu}')

new_tu_one = (10,)
new_tu_two = 10,
print(f'singleton tuples :{new_tu_one} and {new_tu_two}')
print(new_tu_two[0])

tuple_from_range = tuple (range(1,10,1))
print(tuple_from_range)

print('the comma which makes a tuple')
# Note that it is actually the comma which makes a tuple, not the parentheses.
# The parentheses are optional, except in the empty tuple case, or when they are
# needed to avoid syntactic ambiguity. 
new_tu_five = 10, [2,1,2],tuple (range(1,10,1))
print(new_tu_five)



#Text sequence types
#Triple quoted strings may span multiple lines - all associated w
# hitespace will be included in the string literal.
print('Text sequence type')

text_one = 'Single quote with "double quotes" '
text_two = "Double quotes 'single' "
text_three = '''This allow
 multi-line string
  link below'''
text_four = """another approach 
for multi-line """
print(text_one)
print(text_two)
print(text_three)
print(text_four)

print('sreejith'.center(200,'*'))
print('sREejith'.casefold().capitalize())

# more string formattings

print('%(lan)s has %(num)03f quotes types.' % {'lan':'Python', 'num':5})
print('%(lan)s has %(num)02d quotes types.' % {'lan':'Python', 'num':5})


#Binary Sequence Types — bytes, bytearray, memoryview
print(f'Binary Sequence Types bytes, bytearray, memoryview'.center(100,'_'))

b= bytes('Sreejith','utf-8','strict')
print(b)
print(bytes.fromhex('2Ef0 F1f2'))

bytearra=bytearray(b'Hi!')


print(f'Dictionary implementation')


a = dict(one=1, two=2, three=3)
print(a)

b = {'one':1, 'two':2, 'three':3}
print(b)

c= dict(zip(['one','two','three'],[1,2,3]))
print(c)

d = dict([('two', 2), ('one', 1), ('three', 3)])
print(d)

e = dict({'three': 3, 'one': 1, 'two': 2})
print(e)

print(a==b==c==d==e)

print('END')