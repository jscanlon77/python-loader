import pyodbc
import logging
import urllib
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import pandas as pnds
from pandas.core.groupby.groupby import DataError

class SqlProvider:

    def insertRecords(self, df, tableName, isReplace, chSize) :
        replaceOrAppend = ''
        if isReplace :
            replaceOrAppend = 'replace'
        else :
            replaceOrAppend = 'append'
        
        try :
            engine = create_engine("mssql+pyodbc://" + 'LOCALHOST' + "/" + 'InvestorAnalytics' + "?driver=ODBC+Driver+17+for+SQL+Server",
    fast_executemany=True)
            df.to_sql(name=tableName,con=engine, if_exists=replaceOrAppend, index=False,chunksize=chSize)
        except SQLAlchemyError as e :
            logging.error(e)

    def getRecords(self, connectionString, query) :
        
        try:
            genericArray = []

            conn = pyodbc.connect(connectionString)
            cursor = conn.cursor()
            cursor.execute(query)

            
            for row in cursor :
                genericArray.append(row)

            return genericArray
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            logging.error(sqlstate.msg)
        finally :
           
            cursor.close()
            conn.close()

       
