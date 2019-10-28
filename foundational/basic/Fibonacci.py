#Fibonancci numbers module

def fib(n): #function to print fibonancci number series for n
    a, b = 0, 1
    while a < n:
        print(a, end=',')
        a, b = b, a+b
    print('end')

def fib2(n):
    a, b = 0, 1
    result=[]
    while a < n:
        result.append(a)
        a, b= b, a+b
    return result
