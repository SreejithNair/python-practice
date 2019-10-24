
import database_connector as db

try:
    database_instance = db.DatabaseConnector('nor-grputils-01','TheLoansEngineCRM')
except Exception as ex:
    print(ex.args)
else:
    #print(database_instance.get_market_scan(10))
    print(database_instance.migrate_data())
    
    
    