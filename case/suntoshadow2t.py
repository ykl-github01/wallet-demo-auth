from framework.browser_engine import Browser
from framework.basepage import BasePage
from case.login import Login
import configparser,os

driver=Browser().open_browser()
bs=BasePage(driver)
Login().login()
config = configparser.ConfigParser()
dir = os.path.abspath('.').split('case')[0]
config.read(dir + "/config/config.ini", encoding='UTF-8')
w2 = config.get("theWallets", "wallet2")
try:
    driver.find_element_by_css_selector('').send_keys(w2)
    driver.find_element_by_xpath('//*[@id="utxoNormalAmountId"]').send_keys(200)
    driver.find_element_by_xpath('//*[@id="normalTransferButtonId"]').click()
    print('恭喜：A明文转B2TRI成功')
except Exception as e:
    print(e)
    print('转账失败或者余额不足')