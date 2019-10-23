'''
This class helps to connect to a odbc database using the supplied connection string
https://github.com/mkleehammer/pyodbc/wiki/Getting-started
'''
import pyodbc as sql_odbc
import custom_exceptions as ce
import json
import datetime as dt

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
            # print(ex.args)
            # print(ex)
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

    def migrate_data(self, no_of_rows=0):
        try:
            self.__connect_to_database__() # connect to database
            db_cursor = self.__connection_object__.cursor() # grab a cursor

            prefix = 'SELECT distinct' # if no of rows has value then only affect those many otherwise all
            if no_of_rows > 0:
                prefix = 'SELECT distinct top ('+str(no_of_rows)+') '
            sql = prefix + " [URN] FROM MarketScan_1"

            rows = db_cursor.execute(sql).fetchall() # get required data from the source table(source data is mixed up - broker and ifa)

            new_broker_id = 0

            for row in rows:
                source_broker_rows = db_cursor.execute(f"select top(1) * from MarketScan_1 where URN='{row.URN}'").fetchall()  # select one row by URN to create broker

                for b_row in source_broker_rows:
                    sql = 'insert into Broker(NetworkID,Name,PhoneNumber,Website,HouseNumber,Street,Town,County,Postcode,Status,Channel,RegisteredDate) values (?,?,?,?,?,?,?,?,?,?,?,?)'
                    
                    #house keeping to remove invalid data
                    network_id = 62
                    broker_name = '' if b_row.CompanyName is None else b_row.CompanyName
                    phone = '' if b_row.Phone is None else str(b_row.Phone).replace(' ','')
                    website = '' if b_row.Website is None else b_row.Website
                    house_number= '' if b_row.Address1 is None else b_row.Address1
                    street = '' if b_row.Address2 is None else b_row.Address2
                    town = '' if b_row.Town is None else b_row.Town
                    county = '' if b_row.County is None else b_row.County
                    post = '' if b_row.Postcode is None else b_row.Postcode
                    
                    #create a new broker and grab the new id in new_broker_id
                    db_cursor.execute(sql, network_id, broker_name, phone, website, house_number, street, town, county, post, 'Bought Data','Bought Data', dt.datetime.now().strftime('%Y-%m-%d'))
                    self.__connection_object__.commit()
                    new_broker_id = db_cursor.execute('SELECT @@IDENTITY as broker_id').fetchone().broker_id
                
                #now read all data under the URN to create IFA records
                ifa_rows = db_cursor.execute(f"select * from MarketScan_1 where URN='{row.URN}'").fetchall()  # select all row by URN to create IFA

                for ifa_row in ifa_rows:
                    sql = 'insert into IFA(NetworkID,BrokerID,Title,Forename,Surname,OfficeNumber,Email,Status,SubStatus,Username,Password,RegisteredDate,RegisteredBy,Channel,LastCallOutcome) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
                    
                    #house keeping to remove invalid data
                    network_id = 62
                    title = '' if ifa_row.ContactTitle is None else ifa_row.ContactTitle
                    first_name = '' if ifa_row.ContactFirstname is None else ifa_row.ContactFirstname
                    sur_name = '' if ifa_row.ContactSurname is None else ifa_row.ContactSurname
                    phone = '' if ifa_row.Phone is None else str(ifa_row.Phone).replace(' ','')
                    email = '' if ifa_row.ContactEmail is None else ifa_row.ContactEmail
                    user_name = f'{first_name}..{sur_name}..{title}'[:15] #max 15 chars starting from index 0 (default/ step 1 default)
                    password = 'Password123'

                    #create a new broker and grab the new id in new_broker_id
                    db_cursor.execute(sql,network_id,new_broker_id,title,first_name,sur_name,phone,email,'Bought Data','Bought Data',user_name,password,dt.datetime.now().strftime('%Y-%m-%d'),'Kerry Shaw','Bought Data','No contact')
                    self.__connection_object__.commit()

        except Exception as ex:
            raise ex
        else:
            return
        finally:
            self.__connection_object__.close()



