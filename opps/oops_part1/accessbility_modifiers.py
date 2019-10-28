#demonstrate accessibility modifiers

class DemoModifier:

    def __init__(self):
        pass

    def modifier_method(self,name):
        self.name = name #public variables - available inside and outside this module
        self.__age = 36 #private variables - available only inside the class definitions
        self._parent = [] #protected variable - available inside the class and the module.

demo = DemoModifier()
demo.modifier_method('Sreejith')
print(demo.name)
print(demo._parent)
print(demo.__age) # this line will fail with 'DemoModifier' object has no attribute '__age'

