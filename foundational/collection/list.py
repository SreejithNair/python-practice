
new_list = list(range(1,10,1)) # create list using iterator
print(new_list)

new_list_two = [x for x in new_list]
print(new_list_two)

new_list_three = []
print(new_list_three)
new_list_four= [[[1,2],[4,4]],[[1,2,3,4,5],[1,2],[1,0,-1]]]
print(new_list_four)
print(new_list_four[0])

print(new_list_four[1])
for a in new_list_four[1]:
    print(a)

print(new_list_four[1][2])

#delete items from list
print('delete items from list')
items_to_delete = list(range(10,1,-1))
del items_to_delete[2]
print(items_to_delete)

#Pop remove items from list permanantely but return the removed item
first_item = items_to_delete.pop(0)
print(first_item)
print(items_to_delete)
items_to_delete.sort()
print(items_to_delete)
items_to_delete.reverse()
print(items_to_delete)
items_to_delete.reverse()
print(items_to_delete)