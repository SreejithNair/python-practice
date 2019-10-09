print(3.14,'=>', int(3.14)) #3
print(3.9999,'=>', int(3.9999)) #3
print(-3.9999,'=>', int(-3.9999)) #-3
print('18//4','=>', 18//4) #4
print('18.0//4','=>', 18.0//4) #4.0
print('18//4.0','=>', 18//4.0) #4.0
print('12345','=>',int("12345")) #12345


#will fail
#print('123xz45','=>',int("123xz45"))


p = 10000 #principal amount
n = 12 # number of times the interest is compounded per year
r = 8.0/100 #interest rate

#t = int(input('deposit duration in years:'))
t = 2

maturity_amount_after_t = p * (( 1 + r/n) ** (n*t))
print(f'You will get {maturity_amount_after_t} principal+ compound interest after {t} years')

words = 'All work and no play makes Jack a dull boy'
wordsDic = {}
split = words.split(sep=' ')
for k,v in zip(range(0,len(split),1),split):
    wordsDic[k]=v

print(wordsDic)

