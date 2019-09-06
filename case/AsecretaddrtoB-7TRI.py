from framework.basepage import BasePage
from case.login import Login
import configparser,os
import time

'''
A隐私地址转B 3TRI
'''
driver=Login().login()
bs=BasePage(driver)
config = configparser.ConfigParser()
dir = os.path.abspath('.').split('case')[0]
config.read(dir + "/config/config.ini", encoding='UTF-8')
w2 = config.get("theWallets", "wallet2")
try:
    driver.find_element_by_xpath("//*[@id='utxoPrivacyDestAddressId']").send_keys(w2)
    time.sleep(1)
    driver.find_element_by_id('utxoPrivacyAmountId').send_keys(700)
    time.sleep(1)
    driver.find_element_by_id('privacyTransferButtonId').click()
    time.sleep(2)
    driver.switch_to_alert().accept()
    driver.find_element_by_xpath('//*[@id="refreshCurrentBalanceButton"]').click()
    time.sleep(5)
except Exception as e:
    print(e)

driver.quit()