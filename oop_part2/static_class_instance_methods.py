#This demonstrate how we could define following method using function decorators
# instance methods -> usually perform something in a bonded context (instance of a class)
# class method -> perform something at class level and has no bounded context
# static method -> perform a utility function within class and has no relevance outside

class MethodDemo(object):
    instance_counter = 0 #class level variable or think it like static variable
    def __init__(self, value):
        MethodDemo.instance_counter +=1
        self.value = MethodDemo.cleanse_value(value)

    def get_value(self):#instance method
        print(self.value)

    @classmethod
    def get_instace_count(cls):#class method with cls as first argument and @classmethod as decorator
        print(cls.instance_counter)
    
    @staticmethod
    def cleanse_value(value): # static methos with any input value and @staticmethod as function decorator
        if type(value) is int:
            return value
        else:
            return 0

if __name__ == "__main__":
    m = MethodDemo(10)
    m.get_value()
    print(MethodDemo.instance_counter)
    m = MethodDemo('10')
    m.get_value()
    print(MethodDemo.instance_counter)
    print(MethodDemo.cleanse_value(40))
    print(MethodDemo.cleanse_value('Sreejith'))