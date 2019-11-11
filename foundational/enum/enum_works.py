from enum import Enum, unique


class Color(Enum):
    RED=1
    BLUE=2
    GREEN=3

    @classmethod
    def favorate_colour(cls):
        return cls.GREEN.name

    def describe(self):
        return self.name, self.value
    
    def __str__(self):
        return f'Custom colour'

#By default, enumerations allow multiple names as aliases for the same value. But not duplicating names.

# class DuplicateKey(Enum):
#     RED=1,
#     BLUE=2,
#     GREEN=1

#to enforce unique name and value use following attribute

# @unique
# class UniqueMembers(Enum):
#     RED=1
#     BLUE=2
#     GREEN=1

if __name__ == "__main__":
    #x = UniqueMembers.GREEN
    #print(x.value)
    x = Color.GREEN
    print(x.describe())
    print(x)
    print(Color.favorate_colour)

    print(Color.BLUE.value)
    print(Color.BLUE.name)
    print(Color.BLUE)
    for a in Color:
        print(f'Values: {a.value}, Name: {a.name}')    

    input_string = 'Microsoft    Windows     Server 2008  R2  Enterprise'

    print(' '.join(input_string.split()[2:-1]))   
    
    # i= [p for p, char in enumerate(input_string) if char == ' ']
    
    # result = input_string[i[1]: i[-1]].strip()
    
    # print(result)