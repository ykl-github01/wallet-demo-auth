import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Remote(
     command_executor='http://192.168.217.129:4444/wd/hub',
     desired_capabilities=DesiredCapabilities.CHROME)

base_url='http://www.xiami.com/song/1797262971'
driver.get(base_url)
driver.implicitly_wait(300)
driver.find_element_by_link_text('立即播放').click()
time.sleep(6000)
driver.close()
print('that is down')