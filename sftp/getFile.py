import pysftp

class ImportFile :
    def getFileListing(self, host, user, passwd) :
        srv = pysftp.Connection(host=host, username=user,
        password=passwd)

        try:
           data = srv.listdir()
           
           return data
        except IOError as ioError:
            print(ioError)
        finally :
            srv.close()

       