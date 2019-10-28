#polymorphism in python

#method overloading ( as is a dynamic language the overloading is not that relevent )

class MethodOverloadingDemo:

    def method_a(self,age,sex=None):
        if sex is None:
            print('age is not the only factor')
        else:
            if age < 18:
                print('young to vote')
            else:
                print(f'as a {sex} of {age} years old, you have all right to vote!')

m = MethodOverloadingDemo()
m.method_a(16,'Male')
m.method_a(35)
m.method_a(18,'Female')

#method overriding

class Vehicle:
    def print_details(self):
        print('This is parent Vehicle class method')

class Car(Vehicle):
    def print_details(self): #here the method from parent is overrittern
        print('This is Child Vehicle class method')

parent = Vehicle()
parent.print_details()

child = Car()
child.print_details()