#type details
intv = 3
floatv = 9.89
stringv = 'wordme'
shouldPrint = input(f'Type ay key to continue to see type using type(x){__name__}:')
#printing type details
values = f'Integer:{type(intv)}\nFloat:{type(floatv)}\nString:{type(stringv)}\nPrompt:{type(shouldPrint)}'
print(values)

#checking type using isinstance of function to return True/False
input(f'Press any key to use isinstance:')
if isinstance(intv,bool):
    print(f'Variable {intv} is boolean')
else:
    print(f'Variable {intv} is {type(intv)}')

if isinstance(floatv,float):
    print(f'Variable {floatv} is a Float')
elif isinstance(floatv,int):
    print(f'This would never print unless you change the program')
