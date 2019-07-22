# python-loader
This is a generic loader from SFTP to a sql database using 
SQLAlchemy, ODBC drivers.

It loads in a CSV generically, i.e we don't care what the csv file is as long as its valid
and we just give a table name.. I would probably create a staging tables for each csv and then use some kind of ETL
process to put the data into the correct format with correct indexes etc.


