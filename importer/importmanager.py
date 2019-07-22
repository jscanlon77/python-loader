import pandas as pnds
from pandas.core.groupby.groupby import DataError
from database import dataprovider


class ImportFile :

    
    def ProcessCsv(self, fileName, chSize, destinationName) :
        try:
            # Firstly decide how to process the filename based on its type
            # we can use switch/case for this or we can do something more fancy like name matching and function calling
            
            df = pnds.read_csv(fileName)
            prov = dataprovider.SqlProvider()
            prov.insertRecords(df, destinationName, False, chSize)
        except DataError as dataError :
            print(dataError)
