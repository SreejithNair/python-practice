#in order to create an abstract class we must import the abc (abstract base class) module and
#set the __metaclass__ private variable to the value of abc.ABCMeta
#use @abc.abstractmethod function decorator to each abstract method
# You can have abstract class method, abstract instance method and abstract static method
# Abstract classes may not be instantiated, and require subclasses to provide implementations for the abstract
# methods. 

from abc import ABC, abstractmethod

class CustomAbstract(ABC):
   
    def __init__(self):
        super().__init__()

    @abstractmethod
    def set_val(self,value):
        pass

class SubClass(CustomAbstract):
     def set_val(self,value):
        pass

if __name__ == "__main__":
    c = SubClass() # This will throw an exception if we don't override the set_vale function ->TypeError: Can't instantiate abstract class SubClass with abstract methods set_val
   