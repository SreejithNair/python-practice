import enum as Enum

    
class OrderedEnums(Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented
    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

class Grade(OrderedEnums):
    A=5
    B=4
    C=3
    D=2
    E=1
