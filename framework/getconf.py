import configparser
import os
dir = os.path.abspath('.').split('framework')[0]
url=dir + "/config/config.ini"
class GetConf():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(url)

    def getwallet(self,name):
        value=self.config.get('theWallets',name)
        return value