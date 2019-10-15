#An abstract method can have an implementation in the abstract class! 
# Even if they are implemented, designers of subclasses will be forced to override the implementation.
# Like in other cases of "normal" inheritance, the abstract method can be invoked with super() call mechanism.
# This makes it possible to provide some basic functionality in the abstract method, which can be enriched
# by the subclass implementation.

from abc import ABC, abstractmethod

class AbstractBase(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def self_check(self):
        print('I am from base')
class Derived(AbstractBase):
    
    def self_check(self):
        super().self_check()
        print('i am from derived')

if __name__ == "__main__":
    d= Derived()
    d.self_check()