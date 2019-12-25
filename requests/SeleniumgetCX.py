# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


_code_ = input("code:")
_code_ = _code_.split('.')
_selection_ = _code_[1:len(_code_)]
maincode= _code_[0]
size = int(_code_[1])

if size%5==1:
    size = size + 999
else:
    size = size    

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
def login():
    driver.get("https://configurx.it.abb.com/configurx/content/Login.aspx")
    #username = input("CX user-name:")
    driver.find_element_by_id("txtLogin").send_keys("Thomas-tao.wang@cn.abb.com")
    #passwd = input("Cx Password: ")
    driver.find_element_by_id("txtPassword").send_keys("System03")
    driver.find_element_by_id("cmdLogin").click()
    driver.get("https://configurx.it.abb.com/configurx/content/DetailPopupBasket.aspx?CONF=1")
    
    driver.find_element_by_id("cboMarket").click()
    #market = input("please select your market form list ")
    market = input("please enter your market:")
    market = "(USD) "+market
    #print(market)
    Select(driver.find_element_by_xpath("//select")).select_by_visible_text(market)

    #Select(driver.find_element_by_id("cboMarket")).select_by_visible_text(market)
    driver.find_element_by_id("cboMarket").click()
    driver.find_element_by_id("cmdBasket").click()
    
def filtercode():   
    
    time.sleep(1)
    page=driver.get("https://configurx.it.abb.com/CXEngineX/content/jModelList.aspx")
    time.sleep(1)
    driver.find_element_by_id("Cntnt_txtFilterCode").send_keys(maincode)
    driver.find_element_by_id("Cntnt_cmdFilter").click()
    time.sleep(1)
   
    if size>=700:
        bore = maincode+"_700"
    else:
        bore = maincode+"_C"
    driver.find_element_by_link_text(bore).click()

def code_selection():
    #time.sleep(1)
    driver.get("https://configurx.it.abb.com/CXEngineX/Content/JModelConfiguration.aspx")
    time.sleep(1)
    i = 0
    for i in range(len(_selection_)-3):
        dropmenu = "//div[@id='TabMasterContent_ddl_"+str(i)+"']/a"
       
        time.sleep(0.5)
        if driver.find_element_by_xpath(dropmenu).text[0]==_selection_[i]:
            pass
        else:
            driver.find_element_by_xpath(dropmenu).click()
            _tmp_ = "//a[.//td[text()='" +_selection_[i]+"']]"
            time.sleep(1)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,_tmp_))).click()
            i = i+1        
    if _selection_[-1]=='CWY':
        pass
    else:
        driver.find_element_by_xpath("//div[@id='TabMasterContent_ddl_22']/a").click()
        _certificate_ = "//a[.//td[text()='" +_selection_[-1]+"']]"
        time.sleep(1)
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,_certificate_))).click()
    time.sleep(1)
    driver.find_element(By.ID, "Header_cmdSave").click()
    ''' _codevalue_ = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element(By.ID,'Cntnt_txtCopy'))
    print(_codevalue_.text) '''
    time.sleep(2)
    coded_value=driver.find_element_by_id('Cntnt_txtCopy')
    print(coded_value.text)


if __name__ == "__main__":
    
    t1=time.time()
    login()
    filtercode()
    code_selection()
    driver.close()
    t = time.time()-t1
    print(t)

