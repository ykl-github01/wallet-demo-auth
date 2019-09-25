from framework.basepage import BasePage
from framework.getfilename import GetFileName
from case.login import Login
import configparser,os
import time

class AsecretaaddrtoB_7TRI():
    def asecretaddrtob_7tri(self):
        '''
        A隐私地址转B 7TRI
        '''
        driver=Login().login()
        files=GetFileName().getfilename()
        w2=files[1].split('--')[2]
        bs=BasePage(driver)
        # config = configparser.ConfigParser()
        # dir = os.path.abspath('.').split('case')[0]
        # config.read("../config/config.ini", encoding='UTF-8')
        # w2 = config.get("theWallets", "wallet2")
        try:
            driver.find_element_by_xpath("//*[@id='utxoPrivacyDestAddressId']").send_keys(w2)
            driver.implicitly_wait(1)
            driver.find_element_by_id('utxoPrivacyAmountId').send_keys(700)
            driver.implicitly_wait(1)
            driver.find_element_by_id('privacyTransferButtonId').click()
            driver.implicitly_wait(1)
            #driver.switch_to_alert().accept()
            driver.find_element_by_xpath('//*[@id="refreshCurrentBalanceButton"]').click()
            time.sleep(10)
        except Exception as e:
            print(e)

        driver.quit()
