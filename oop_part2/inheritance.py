class Vehicle(object):
    def __init__(self,name):
        self.name=name

class Car(Vehicle):
    def start(self):
        print(self.name+' started.')

class Van(Vehicle):
    pass


if __name__ == "__main__":
    v = Car('somename')
    v.start()