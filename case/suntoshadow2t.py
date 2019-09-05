from framework.browser_engine import Browser
from framework.basepage import BasePage
from case.login import Login

driver=Browser().open_browser()
bs=BasePage(driver)
Login().login()