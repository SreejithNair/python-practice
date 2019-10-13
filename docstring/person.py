#Class demo with doc string

#Following doc string will give module definition for the consuming script
'''
This module is created for demonstrating docstring
'''
class Person(object):
    '''
    This class represent a blue print for Person object.

    :param name: pass name of the person
    :type name: str.
    '''
    #above class level docstring provide class level description and mandatory parameter and type details
    def __init__(self,name):
        print('person object initialized')
        self.name = name

    def get_name(self):
        ''' This method print the passed in name
        '''
        print(self.name)

    def get_new_name(self,new_name):
        ''' This method print the passed in name
        :param new_name: pass new name of the person
        :typr new_name: str
        '''
        self.name = new_name
        print(self.name)

print(__doc__)
#help(Person)
#help(type(Person))

if __name__ == "__main__":
    p = Person('name')
    p.get_name()
    p.get_new_name('some other name')