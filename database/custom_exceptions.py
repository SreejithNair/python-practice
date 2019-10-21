
import datetime as dt

class CustomException(Exception):
    
    message = f'This is a custom message raised at {dt.datetime}. '

    def __init__(self, message):
        self.message += message
    
    def __str__(self):
        return self.message


class ValueNone(CustomException):

    def __init__(self, message):
      super(ValueNone,self).__init__(message)

    def __str__(self):
        return self.message


class ValueNotRecognized(CustomException):
    def __init__(self, message):
        super(ValueNotRecognized,self).__init__(message)
        
    def __str__(self):
        return self.message
