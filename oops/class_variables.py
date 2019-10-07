# There are two types of Python attributes, instance attributes, and class attributes. The attributes of a class are also referred to as variables
# Local variables are accessible depending on the scope it define
# Instance level variable are referenced with the help of self keyword and is available through out the definitions.
# Global variables for Class is like static variable which are accessible by class name and is global to all instance of a given type.

class GlobalVariables:
    
    instance_count = 0

    def __init__(self):
        GlobalVariables.instance_count+=1

print(f'instance count : {GlobalVariables.instance_count}') #0
g = GlobalVariables()
print(f'instance count : {GlobalVariables.instance_count}')#1
g = GlobalVariables()
print(f'instance count : {GlobalVariables.instance_count}')#2

class InstanceVariables:

    def __init__(self):
        pass

    def capture_instance_values(self, age, sex): #python is dynamically typed language and in order to create instance level variable use
         #self keyword and self to reference it back inside class definition. dot operator if you want to access through the instance.
        self.age = age
        self.sex = sex

instance_variable = InstanceVariables()
instance_variable.capture_instance_values(37,'Male')
print(f'Age:{instance_variable.age} and sex: {instance_variable.sex}')

class LocalVariable:

    def test_method(self):
        count = 0
        return count

l = LocalVariable()

print(f'Get local variable value:{l.count}') # this will fail with LocalVariable' object has no attribute 'count'

#https://stackabuse.com/object-oriented-programming-in-python/
