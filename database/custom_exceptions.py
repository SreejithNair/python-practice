
import datetime as dt

class CustomException(Exception):
    
    message:str = f'This is a custom message raised at '

    def __init__(self, message):
        self.message += message
    
    def __str__(self):
        return self.message + self.get_date_time()
    
    def get_date_time(self):
        return dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


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
