from framework.browser_engine import Browser
from framework.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import win32gui
import win32con
import win32api
import time

driver=Browser().open_browser()
driver.get('http://192.168.1.141:3000/')
wait = WebDriverWait(driver, 10)
temp = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="LoadFromFileId"]')))
driver.find_element_by_xpath('//*[@id="LoadFromFileId"]').send_keys(r'E:\t_login\UTC--2019-09-04T07-58-04-244Z--24Wyp1K7nztULsaGHWSC68QiLvRPY9K5WYFCo2yxnCVpKdGsU7c8ouzjqt5joJuQhMDds9hNMPVjg1TM8MCXLrbz')
time.sleep(3)


'''
dialog = win32gui.FindWindow('#32770', u'文件上传')
ComboBoxEx = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx, 0, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
button = win32gui.FindWindowEx(dialog, 0, 'Button', None)

win32gui.SendMessage(Edit, win32con.WM_SETTEXT, 0,"E:/t_login/UTC--2019-09-04T07-58-04-244Z--24Wyp1K7nztULsaGHWSC68QiLvRPY9K5WYFCo2yxnCVpKdGsU7c8ouzjqt5joJuQhMDds9hNMPVjg1TM8MCXLrbz")

win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
'''

'''
dialog = win32gui.FindWindow('#32770', u'文件上传')  # 识别对话框句柄，我的对话框名字就叫“打开”，火狐'文件上传'
time.sleep(2)
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
time.sleep(2)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
time.sleep(2)

Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 找到输入框Edit对象的句柄
time.sleep(2)
button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 找到按钮Button
time.sleep(2)
win32gui.SendMessage(Edit, win32con.WM_SETTEXT,0, r'E:/t_login/UTC--2019-09-04T07-58-04-244Z--24Wyp1K7nztULsaGHWSC68QiLvRPY9K5WYFCo2yxnCVpKdGsU7c8ouzjqt5joJuQhMDds9hNMPVjg1TM8MCXLrbz')  # 往输入框输入绝对地址
time.sleep(2)
win32api.keybd_event(13, win32con.KEYEVENTF_KEYUP, 0)  # 按下button
#win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button，用这种的我的存在一点问题，就是上传以后浏览器整个卡住了，所以用了上面的一种
'''