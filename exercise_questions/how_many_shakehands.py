#How many handshakes would it take for everyone in your class to shake hands with everyone else? 
# You should not shake hands with the any person twice and you don’t shake your own hand.
#A,B = 1 handshakes
#ABC => => 3 handshakes
#ABCD => 6 handshakes
#ABCDE => 10 handshakes
#ABCDEF => 15 handshakes
#http://www.math.cmu.edu/~bkell/21110-2010s/formula.html

def get_number_of_handshake(no):
    if no <= 1:
        return 0
    if no == 2:
        return 1
    if no > 2:
        x = n-1

    return no * fact_func(no-1)

def no_of_handshakes(no_of_students):
    if no_of_students <=1:
        return 0
    

cnt = 0
while cnt < 5:
    no_of_students = int(input('Number of students in class:'))
    if no_of_students <=1:
        continue
    print(f'Total handshakes are:{fact_func(no_of_students)}')
    cnt+=1

