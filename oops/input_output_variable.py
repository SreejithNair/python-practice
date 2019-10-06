#demonstrate instance level and class level variable
#the instance attributes are referred using the self keyword, 
# while class attributes are referred by the class name.

class Car:
    total_cars_count=0

    @staticmethod #To declare a static method, you have to specify the @staticmethod descriptor before the name of the method
    def get_cars_count_sofar():
        print(Car.total_cars_count)# It is important to mention that static methods can only access class attributes in Python.

    def __init__(self):
        pass

    def name_the_car(self,car_name):
        self.car_name = car_name
        Car.total_cars_count += 1

    def get_count(self):
        print(total_cars_count)

    def __str__(self):
        print(f'Current car count: {Car.total_cars_count} and name :{self.car_name}')

car = Car()
car.name_the_car('Audi')
car.__str__()

car2 = Car()
car2.name_the_car('Nissan')
car2.__str__()

Car.get_cars_count_sofar()