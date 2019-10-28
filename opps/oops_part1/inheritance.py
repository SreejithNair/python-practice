#inheritance from a single base and multiple inheritance

class Parent:
    
    def __init__(self):
        print('Parent constructor called')
    
    def parent_method(self):
        print('Parent method called')

class ChildA:
    def __init__(self):
        print('Child A constructor called')

    def child_a_method(self):
        print('Child A method called')

class ChildB:
    def __init__(self):
        print('Child B constructor called')

    def child_b_method(self):
        print('Child B method called')

p = Parent() # Parent constructor called
p.parent_method() #Parent method called

ca = ChildA() #Child A constructor called
ca.child_a_method() #Child A method called

class ChildC(Parent):
    def __init__(self):
        print('Child C constructor called')
    
    def child_c_method(self):
        print('Child C method called')
print()

#following with print
#Child C constructor called
#Parent method called
#Child C method called

c = ChildC()
c.parent_method()
c.child_c_method()

class Camera:
    def camera_method(self):
        print("This is parent Camera class method")

class Radio:
    def radio_method(self):
        print("This is parent Radio class method")

class CellPhone(Camera, Radio):
     def cell_phone_method(self):
        print("This is child CellPhone class method")

#This is parent Camera class method
#This is parent Radio class method
#This is child CellPhone class method

cell_phone_a = CellPhone()
cell_phone_a.camera_method()
cell_phone_a.radio_method()
cell_phone_a.cell_phone_method()