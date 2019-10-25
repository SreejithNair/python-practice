#string
#string is a sequence of immutable characters (any action on initial variable will cause to create new variable to store the output)
print('String-https://www.geeksforgeeks.org/python-strings/')
print('*'*6)
value = 'This is the string'
print(value.__hash__())
value = value[:5]
print(value.__hash__())
print(value)
print(value.__hash__())
print("\n")
print("\n")

print('Playing with string')
new_string = 'Welcome'
print('0th Index: ' +new_string[0])
print('last Index: ' +new_string[new_string.__len__()-1])
print('last Index: ' +new_string[-1])
print('last Index: ' +new_string[-2])
print('last Index: ' +new_string[-3])
print('last Index: ' +new_string[-1*new_string.__len__()])
print("\n")
print("\n")


print('Slicing string')
sliced = new_string[0:1]
print(sliced)
sliced = new_string[:3]
print(sliced)
sliced = new_string[:-1*new_string.__len__()]
print(sliced)
print("\n")
print("\n")

#Updating or deleting a character in a string is not possible and cause system to throw error.
#However, we can delete the entire string using del keyword
del sliced

print('formatting')
val="{0:b}".format(23) # binary representation of 23
print(val)
val="{0:e}".format(23) # exponential represention of 23
print(val)
val="{0:.2f}".format(23/3) # result round to 2 decimal
print(val)
print("\n")
print("\n")

print('String alignment')
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks','for','Geeks') 
print("\nLeft, center and right alignment with Formatting: ") 
print(String1)

# To demonstrate aligning of spaces  
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009) 
print(String1)

print("\n")
print("\n")

