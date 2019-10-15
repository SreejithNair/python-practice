import random

class Animal(object):

    def __init__(self, name):
        self.name = name

class Dog(Animal):

#Possible
    # def __init__(self,name):
    #     Animal(Dog,self).__init__(name)
    #     self.breed = random.choice(['Shih Tzu', 'Beagle','Mutt'])

#Preffered
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Shih Tzu', 'Beagle','Mutt'])

    def fetch(self, thing):
        print(f'My {self.name} goes after {thing}. His breed is {self.breed}.')

if __name__ == "__main__":
    dog = Dog('Puppy')
    dog.fetch('ball')