from framework.basepage import BasePage
from framework.getfilename import GetFileName
from case.login import Login
import configparser,os
import time

class AsecretaaddrtoB_3TRI():
    def asecretaddrtob_3tri(self):
        '''
        A隐私地址转B 3TRI
        '''
        driver=Login().login()
        bs=BasePage(driver)
        files=GetFileName().getfilename()
        w2=files[1].split('--')[2]
        # config = configparser.ConfigParser()
        # dir = os.path.abspath('.').split('case')[0]
        # config.read("../config/config.ini", encoding='UTF-8')
        # w2 = config.get("theWallets", "wallet2")
        try:
            driver.find_element_by_xpath("//*[@id='utxoPrivacyDestAddressId']").send_keys(w2)
            time.sleep(1)
            driver.find_element_by_id('utxoPrivacyAmountId').send_keys(300)
            time.sleep(1)
            driver.find_element_by_id('privacyTransferButtonId').click()
            time.sleep(1)
            #driver.switch_to_alert().accept()
            driver.find_element_by_xpath('//*[@id="refreshCurrentBalanceButton"]').click()
            time.sleep(10)
        except Exception as e:
            print(e)

        driver.quit()