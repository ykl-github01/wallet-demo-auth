from framework.browser_engine import Browser
from framework.basepage import BasePage
from framework.readexcel import ReadExcle
import os

driver=Browser().open_browser()
b=BasePage(driver) #creat BasePage instance
excel_dir = os.path.abspath('.').split('case')[0]+'PageRlements\\elements.xlsx'
r=ReadExcle(excel_dir) #creat ReadExcel instance
excel_list=r.read(sheetname='Sheet1',n=2,num=2)
print(list(excel_list))
upload=b.find_element(id=excel_list[0])

