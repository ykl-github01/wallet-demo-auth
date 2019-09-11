import configparser
import os

class GetConf():
    def __init__(self):
        self.config = configparser.ConfigParser()
        dir = os.path.abspath('.').split('framework')[0]
        self.config.read(dir + "/config/config.ini", encoding='UTF-8')

    def getwallet(self,name):
        value=self.config.get('theWallets',name)
        return value