#https://www.python.org/dev/peps/pep-0008/

class CodeStyle:
    public_variable = 10 # public variable
    _private_variable = 10 # instance level
    __variable_notused_in_subclass = 10 # not even sub class should use this
    __wrong_name__=10 # allocated for magic methods/attributes
