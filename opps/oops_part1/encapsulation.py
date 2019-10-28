#Encapsulation refers data hiding. One class should not have direct access to the data of the other class.
# Rather, the access should be controlled via class methods. To provide controlled access to class data in Python,
# the access modifiers and properties are used.

# read accessibility_modifier.py for access modifier

#following demostrate properties to control data access

#Idea is to restrict the input value (model) from allowed range of values

# Creates class Car
class Car:

    # Creates Car class constructor
    def __init__(self, value):
        # initialize instance variables
        self.model = value

    # Creates model property
    @property
    def model(self):
        return self.__model

    # Create property setter
    @model.setter
    def model(self, value):
        if value < 2000:
            self.__model = 2000
            return
        elif value > 2018:
            self.__model = 2018
            return
        else:
            self.__model = value

    def getCarModel(self):
        return "The car model is " + str(self.model)
    
carA = Car(2088)
print(carA.getCarModel())

print(carA.model)

