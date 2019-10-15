from framework.browser_engine import Browser
from framework.basepage import BasePage
import time
import framework.getconf
from framework.getfilename import GetFileName

class GetSecretCoin():
    def getsecretcoin(self):
        driver=Browser().open_browser()
        bs=BasePage(driver)
        driver.get('http://192.168.1.141:3001/')
        files=GetFileName().getfilename()
        w1=files[0].split('--')[2]
        #w1=framework.getconf.GetConf().getwallet('wallet1')
        time.sleep(2)
        bs.find_element('name<=>user').send_keys(w1)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div/div/form/div[2]/label').click()
        time.sleep(2)
        for i in range(1):
            bs.find_element('classname<=>content-form-signup').click()
        driver.quit()