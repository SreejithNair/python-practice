
class Person(object):
    def __init__(self,name):
        self.name=name
    
    def print_name(self):
        print(f'Name of the person is {self.name}')
    
    def get_name(self):
        return self.name

if __name__ == "__main__":
    print('Person is running from person.py')
    p = Person('Sreejith')
    p.print_name()
else:
    print('Person script is imported by someone')
