from importer import importmanager
import logging
import datetime

importing = importmanager.ImportFile()

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
currentdate = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
logging.info(currentdate)
importing.ProcessCsv(r'C:\Sales\Sales.csv', 2000, 'Sales')
currentdate = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
logging.info(currentdate)


