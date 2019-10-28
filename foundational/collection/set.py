simple_set = {'sr','ee','jith'}
print(f'Len of set is {len(simple_set)}')

frozen_set = frozenset({'sr','ee','jith'})
print(f'Len of frozenset is {len(frozen_set)}')

difference1=frozen_set-simple_set
difference2=simple_set-frozen_set

simple_set.add('an')
simple_set.add('ay')
simple_set.add('ya')
simple_set.add('ya')

print(f'Len of difference1 is {len(difference1)}')
print(f'Len of difference2 is {len(difference2)}')


for z in difference1:
    print(z)

for z in difference2:
    print(z)

print(f'Set union operations')
print (simple_set|frozen_set)

#create a subset

subset_value = simple_set.add('last entry')
print (simple_set)

current_record_pointer = len(simple_set)

print(f'Type of Range function:{type(range(10,30,5))}')
for x in range(10,30,5):
    print(x)

for x in set(range(10,-10,-1)):
    print(x)

