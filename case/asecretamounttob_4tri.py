from framework.basepage import BasePage
from framework.getfilename import GetFileName
from case.login import Login
import configparser,os
import time
class AsecretamounttoB_4TRI():
    def asecretamounttob_4tri(self,tri):
        '''
        A隐私金额转B 4TRI
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
            driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/div[1]/input").send_keys(w2)
            driver.implicitly_wait(3)
            driver.find_element_by_id('utxoNormalAmountId').send_keys(tri)
            driver.implicitly_wait(1)
            bs.find_element('id<=>hideNormalAmount').click()
            driver.implicitly_wait(1)
            driver.find_element_by_id('normalTransferButtonId').click()
            driver.implicitly_wait(1)
            #driver.switch_to_alert().accept()
            driver.find_element_by_xpath('//*[@id="refreshCurrentBalanceButton"]').click()
            time.sleep(10)
        except Exception as e:
            print(e)

        driver.quit()