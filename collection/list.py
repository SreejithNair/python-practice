
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
