from framework.browser_engine import Browser
from framework.basepage import BasePage
import time
import framework.getconf

class GetSecretCoin():
    def getsecretcoin(self):
        driver=Browser().open_browser()
        bs=BasePage(driver)
        driver.get('http://192.168.1.141:3001/')
        w1=framework.getconf.GetConf().getwallet('wallet1')
        time.sleep(2)
        bs.find_element('name<=>user').send_keys(w1)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div/div/form/div[2]/label').click()
        time.sleep(2)
        for i in range(0,10):
            bs.find_element('classname<=>content-form-signup').click()
        driver.quit()