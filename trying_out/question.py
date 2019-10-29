
from pandas import DataFrame
import numpy as np

firstProductSet = {'ProductName': ['Computer','Printer'],
                   'SalesOne': [10,8]
                   }
firstDf = DataFrame(firstProductSet,columns= ['ProductName', 'SalesOne'])


secondProductSet = {'ProductName': ['Computer','Printer'],
                   'SalesTwo': [20,12]
                   }
secondDf = DataFrame(secondProductSet,columns= ['ProductName', 'SalesTwo'])


firstDf['SalesOne'] = secondDf['SalesTwo'] 

firstDf['DoesMatch'] = np.where(firstDf.SalesOne == secondDf.SalesTwo, 'True', 'False')  
print (firstDf)
