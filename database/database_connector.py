'''
This class helps to connect to a odbc database using the supplied connection string

'''
import pyodbc as sql_odbc
import custom_exceptions as ce

class DatabaseConnector(object):

    def __init__(connectionString: str) -> str:
        if self.__is_none__(connectionString) or connectionString == '':
            raise ce.ValueNone("Supplied connection string is not valid")

    def connect_to_database(self):
        result = False
        self.__connection_object__ = sql_odbc.connect(f'Driver')
        return result

    def GetData(self, table_name, no_of_rows):
        pass

    #define a private method to valid date

    def __is_none__(self,value,type):
        return if value is None

