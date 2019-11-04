class SomeClass(object):

    def __init__(self):
        pass

    def print(self):
        print(f'')

    def __enter__(self):
        print(f'This will be called upon object creation.')
    
    def __exit__(self, type, value, traceback): #it is mandatory to define error type, value and traceback
        print(f'this will be called when object gors out of scope')

with SomeClass() as sm:
    sm.print()

