from selenium import webdriver
import time
class CreatWallet(object):
    def creat_wallet(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.dir', r'E:\t_login')
        profile.set_preference('browser.download.folderList', 2)
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/json')


        driver = webdriver.Firefox(firefox_profile=profile)

        driver.get('http://192.168.1.141:3000/')
        time.sleep(3)
        driver.find_element_by_id('CreateAccId').click()
        driver.implicitly_wait(1)
        driver.find_element_by_id('downloadAccountFileId').click()
        time.sleep(1)
        driver.quit()