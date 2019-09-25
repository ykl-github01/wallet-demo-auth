from framework.browser_engine import Browser
from framework.basepage import BasePage
from framework.getconf import GetConf
import time
class GetCoin():
    def getcoin(self):
        driver=Browser().open_browser()
        bs=BasePage(driver)
        driver.get('http://192.168.1.141:3001/')

        #config = configparser.ConfigParser()
        #dir = os.path.abspath('.').split('case')[0]
        #config.read(dir + "/config/config.ini", encoding='UTF-8')
        #config.read("../config/config.ini", encoding='UTF-8')
        #w1 = config.get("theWallets", "wallet1")
        a=GetConf().getwallet('wallet1')
        print(a)
        time.sleep(2)
        driver.find_element_by_name('user').send_keys(a)
        '''
        待调试
        g=GetConf()
        w1=g.getconf("theWallets","wallet1")
        print(w1)
        bs.find_element('name<=>user').send_keys(w1)
        '''
        '''
        creat 100 coin
        '''
        for i in range(10):
            bs.find_element('classname<=>content-form-signup').click()
        driver.quit()
