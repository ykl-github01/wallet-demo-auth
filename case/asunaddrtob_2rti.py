from framework.basepage import BasePage
from case.login import Login
import configparser,os
import time
from framework.getfilename import GetFileName

class AsunaddrtoB_2TRI():
    def asunaddrtob_2tri(self):
        '''
        A明文转B 2TRI
        '''
        driver=Login().login()
        bs=BasePage(driver)
        config = configparser.ConfigParser()
        files=GetFileName().getfilename()
        v=files[1].split('--')[2]
        # dir = os.path.abspath('.').split('case')[0]
        # config.read( "../config/config.ini", encoding='UTF-8')
        # w2 = config.get("theWallets", "wallet2")
        try:
            driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/div[1]/input").send_keys(v)
            time.sleep(3)
            driver.find_element_by_id('utxoNormalAmountId').send_keys(200)
            time.sleep(2)
            driver.find_element_by_id('normalTransferButtonId').click()
            time.sleep(2)
            #driver.switch_to_alert().accept()
            driver.find_element_by_xpath('//*[@id="refreshCurrentBalanceButton"]').click()
            time.sleep(10)
        except Exception as e:
            print(e)
        driver.quit()