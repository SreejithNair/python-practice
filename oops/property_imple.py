#property

class PropertyImplementation:

    def __init__(self, name, age, sex):
        self.age_pro = age
        self.name_pro = name
        self.sex_pro = sex
    
    @property
    def age_pro(self):
        return self.__age_pro
    
    @property
    def name_pro(self):
        return self.__name_pro
    
    @property
    def sex_pro(self):
        return self.__sex_pro
    
    @name_pro.setter
    def name_pro(self, value):
        self.__name_pro=value
    
    @sex_pro.setter
    def sex_pro(self, value):
        self.__sex_pro=value
    
    @age_pro.setter
    def age_pro(self, value):
        self.__age_pro=value


p = PropertyImplementation('sree',36,'Male')
print(p.name_pro)
print(p.age_pro)
print(p.sex_pro)
p.name_pro='Anay'
p.age_pro=4
p.sex_pro='Male'
print(p.name_pro)
print(p.age_pro)
print(p.sex_pro)



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