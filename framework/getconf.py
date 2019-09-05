import configparser
import os

class GetConf():
    def getconf(self,se,value):
        config = configparser.ConfigParser()
        dir = os.path.abspath('.').split('framework')[0]
        config.read(dir + "/config/config.ini", encoding='UTF-8')
        conf= config.get(se, value)
        return conf
