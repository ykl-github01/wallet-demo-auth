import os
class GetFileName():
    def getfilename(self):
        for root,dir,files in os.walk('E://t_login'):
            return files
