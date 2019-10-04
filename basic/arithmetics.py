import cmath

print(f'Division\n\n=>')
print(f'Division :{5/2}')
print(f'Division return whole number :{5//2}')
print(f'Modules return whole reminder :{5%2}')

print(f'Multiplication\n\n=>')
print(f'Multiplication:{5*2}')
print(f'Power function:{2**3}')

#boolean operator

if 5 == 5 and 6 > 7:
    print(f'Statement is True')
else:
    print(f'Statement is False')

if 'sree' == 'Sree':
    print(f'String comparision is NOT case insensitive')
else:
    print(f'String comparision is case insensitive')

if 5 == 5 or 5 ==9:
    print(f'Statement is True')
else:
    print(f'Statement is False')

if 10 in [1,2,10]:
    print(f'10 in the collection')

if 'sree' in ['jith',3,78.34,'sree']:
    print(f'sree in the collection')

print(f"Rational number: {type(1)}")
print(f"Irrational number: {type(2.3)}")
#print(f'Complex number number: {type(complex('3+2*i'))}')

#print(complex('3+2*i'))

x = 10
y = 3

z= complex(x,y)
a=z.conjugate()
print(f'real part:{z.real} and imaginary:{z.imag}')
print(f'Conjugate of above complex. Real:{a.real} and imaginary:{a.imag}')
    
    
print(divmod(5,2))
    