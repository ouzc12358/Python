# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import bs4 as bs
import requests


def clean_mark(s):
    s=s.replace('.','')
    s=s.replace('-','')
    return s 
b = input("code:")
a = clean_mark(b)
maincode = a[0:6]
size =int(a[6:9])
letter = a[9:27]
language = a[27:29]
verification = a[29:31]
certificate =a[31:34]

driver=webdriver.Chrome()
''' chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options) '''
def login():
    driver.get("https://configurx.it.abb.com/configurx/content/Login.aspx")
    #username = input("CX user-name:")
    driver.find_element_by_id("txtLogin").send_keys("Thomas-tao.wang@cn.abb.com")
    #passwd = input("Cx Password: ")
    driver.find_element_by_id("txtPassword").send_keys("System02")
    driver.find_element_by_id("cmdLogin").click()
    driver.get("https://configurx.it.abb.com/configurx/content/DetailPopupBasket.aspx?CONF=1")
    driver.find_element_by_id("cboMarket").click()
    Select(driver.find_element_by_id("cboMarket")).select_by_visible_text("(USD) USA")
    driver.find_element_by_id("cboMarket").click()
    driver.find_element_by_id("cmdBasket").click()
    
def filtercode():   
    
    time.sleep(1)
    page=driver.get("https://configurx.it.abb.com/CXEngineX/content/jModelList.aspx")
    #driver.find_element_by_id("Cntnt_txtFilterCode").clear()
    #maincode = input("输入主code:")
    driver.find_element_by_id("Cntnt_txtFilterCode").send_keys(maincode)
    
    driver.find_element_by_id("Cntnt_cmdFilter").click()
    time.sleep(2)
   
    if size>=700:
        driver.find_element_by_link_text("FEW315_700").click()
    else:
        driver.find_element_by_link_text("FEW315_C").click()
    

def code_selection():
    driver.get("https://configurx.it.abb.com/CXEngineX/Content/JModelConfiguration.aspx")
      
    #time.sleep(1)
    driver.find_element_by_link_text("700 : DN 700 (28 in.)").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".chRow:nth-child(4) .chC2p").click()
    time.sleep(1)
    driver.find_element_by_link_text("H : Hard Rubber").click()   
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".chC2p").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "1 : Standard").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".chSC2p").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "S : Stainless steel 316").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".chRow:nth-child(2) .chC2p").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "C2 : Flanges AWWA C207 Class D").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".chRow:nth-child(4) .chC2p").click()
    time.sleep(1)
    driver.find_element(By.ID, "Header_cmdSave").click()
    time.sleep(3)
    coded_value=driver.find_element_by_id('Cntnt_txtCopy')
    print(coded_value.text)
    
if __name__ == "__main__":
    login()
    filtercode()
    code_selection()
    driver.close()
