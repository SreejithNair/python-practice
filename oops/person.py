
#Person

class Person:
    def __init__(self):
        pass
    def get_age(self, age=18, *args):
        print(f'You provided: {age} and args: {args}')
    def another_method(self):
        pass

    def another_age(self,*args,**kvs):
        print(args)
        print(kvs)

person = Person()
person.get_age(10,'Sreejith',37,{'K':1,'L':2})
person.another_age(args:30,40,45,234,234,111,kvs:{'one':1,'two':2})