class Animal(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'{self.name} eats {food}.')
    
    def make_sound(self):
        pass

class Dog(Animal):

    def fetch(self,thing):
        print(f'{self.name} goes after the {thing}!.')
    
    def show_affection(self):
        print(f'{self.name} wags tail.')
    
    def make_sound(self):
        print(f'{self.name} barks!')

class Cat(Animal):

    def show_affection(self):
        print(f'{self.name} purrs')

    def swatstring(self):
        print(f'{self.name} shreds the string!')
        
    def make_sound(self):
        print(f'{self.name} meow!')

if __name__ == "__main__":
    for obj in [Dog('Rover'), Cat('Fluffy'), Cat('Precious'), Dog('Scout')]:
        obj.show_affection()
        obj.make_sound()
