#demostrate how to pass variable and return values

class Parameter:

    def single_input_output(self,name):
        return name

    def multiple_input_outpur(self, age1, age2, age3):
        return age1*age1, age2*age2, age3*age3

#The special syntax *args in function definitions in python is 
# used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, 
# variable-length argument list.
    def variable_input_outpur(self, *args):
        return args

#Using the *, the variable that we associate with the * becomes an iterable (tuple instance) 
# meaning you can do things like iterate over it
    def variable_input_extract(self, *args):
        for x in args:
            print(f'{x}\n')

#The special syntax **kwargs in function definitions in python is used to pass a keyworded,
# variable-length argument list. We use the name kwargs with the double star.
    def variable_input_keyword(self, **kwargs):
        for x,y in kwargs.items():
            print(f'Key:{x} Value:{y}')

single_para = Parameter().single_input_output('Input Value')
print(single_para)

multi_para = Parameter().multiple_input_outpur(2,4,6)
print(multi_para)

variable_para = Parameter().variable_input_outpur(10,20,'Sree',234.2233,'another')
print(variable_para)

variable_para = Parameter().variable_input_extract(10,20,'Sree',234.2233,'another')

keyworded_input = Parameter().variable_input_keyword(first=30, second=50, third=70)