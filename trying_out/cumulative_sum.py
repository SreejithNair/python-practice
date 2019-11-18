class DatabaseConnector(object):
    def __init__(self, server_name: str, database_name:str, driver_name:str='SQL Server') -> str:
        connetion_string = f'DRIVER=SQL Server;SERVER=YourServerName;DATABASE=YourDatabaseName;UID=YourSQLOrDomainUserName;PWD=YourPassword;TRUSTED_CONNECTION=yes;'
        self.__connection_object= sql_odbc.connect(connetion_string)