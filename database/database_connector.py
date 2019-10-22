'''
This class helps to connect to a odbc database using the supplied connection string
https://github.com/mkleehammer/pyodbc/wiki/Getting-started
'''
import pyodbc as sql_odbc
import custom_exceptions as ce
import json

class DatabaseConnector(object):

    def __is_none__(self, value):

        if value is None:
            return True
        else:
            return False


    def __init__(self, server_name: str, database_name:str, driver_name:str='SQL Server') -> str:

        try:
            if self.__is_none__(server_name) or server_name == '':
                raise ce.ValueNone("Supplied server name string is not valid")
            
            if self.__is_none__(database_name) or database_name == '':
                raise ce.ValueNone("Supplied database name string is not valid")

            if self.__is_none__(driver_name) or driver_name == '':
                raise ce.ValueNone("Supplied driver name string is not valid")

        except ValueError as v:
            print(v.args)
            print(v)

        else:
            self.server_name = server_name
            self.database_name = database_name
            self.driver_name = driver_name

    
    def show_all_drivers(self):
        for driver in sql_odbc.drivers():
            print(driver)

    def __connect_to_database__(self):
        try:
            connetion_string = f'DRIVER={self.driver_name};SERVER={self.server_name};DATABASE={self.database_name};UID=ncit\sreejith.nair;PWD=#Carmania#987;TRUSTED_CONNECTION=yes;'
            self.__connection_object__ = sql_odbc.connect(connetion_string)
        except Exception as ex:
            print(ex.args)
            print(ex)
            raise ex        

    def get_market_scan(self, no_of_rows=0):
        
        try:
            self.__connect_to_database__()
            db_cursor = self.__connection_object__.cursor()
            prefix = 'select '
            if no_of_rows > 0:
                prefix = 'select top ('+str(no_of_rows)+')' 
            query = prefix+ '[URN]'\
                            ',[CompanyName]'\
                            ',[Address1]'\
                            ',[Address2]'\
                            ',[Town]'\
                            ',[County]'\
                            ',[Postcode]'\
                            ',[Phone]'\
                            ',[Website]'\
                            ',[ContactTitle]'\
                            ',[ContactFirstname]'\
                            ',[ContactSurname]'\
                            ',[ContactEmail] from MarketScan_1 order by[URN]'
                #print(query)
            db_cursor.execute(query)
            rows =  db_cursor.fetchall()
            #print(db_cursor)    
        except Exception as ex:
            print(ex)
        
        else:
            return rows
        finally:
            db_cursor.close()
            self.__connection_object__.close()
            #print(db_cursor)    
