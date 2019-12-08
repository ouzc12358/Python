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
#from seleniumwire import webdriver



#driver=webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
def login():
    driver.get("https://configurx.it.abb.com/configurx/content/Login.aspx")
    # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
    driver.find_element_by_id("txtLogin").click()
    driver.find_element_by_id("txtLogin").clear()
    driver.find_element_by_id("txtLogin").send_keys("Thomas-tao.wang@cn.abb.com")
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='User Name:'])[1]/following::tr[1]").click()
    driver.find_element_by_id("txtPassword").clear()
    driver.find_element_by_id("txtPassword").send_keys("System02")
    driver.find_element_by_id("cmdLogin").click()
    # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
    driver.get("https://configurx.it.abb.com/configurx/content/DetailPopupBasket.aspx?CONF=1")
    """ driver.find_element_by_id("x1x1").click()
    driver.find_element_by_id("x1x1x1").click() """
    # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
    # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=2 | ]]
    driver.find_element_by_id("cboMarket").click()
    Select(driver.find_element_by_id("cboMarket")).select_by_visible_text("(USD) USA")
    driver.find_element_by_id("cboMarket").click()
    driver.find_element_by_id("cmdBasket").click()
    
def filtercode():   
    # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
    # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
    time.sleep(7)
    page=driver.get("https://configurx.it.abb.com/CXEngineX/content/jModelList.aspx")
    #driver.find_element_by_id("Cntnt_txtFilterCode").click()
    driver.find_element_by_id("Cntnt_txtFilterCode").clear()
    driver.find_element_by_id("Cntnt_txtFilterCode").send_keys("FEW315")
    #driver.find_element_by_id("form1").submit()
    driver.find_element_by_id("Cntnt_cmdFilter").click()
    time.sleep(1)
    driver.find_element_by_link_text("FEW315_700").click()
    #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Standard LeadTime:'])[1]/following::td[1]").click()
    

def code_selection():
    driver.get("https://configurx.it.abb.com/CXEngineX/Content/JModelConfiguration.aspx")
    page=driver.page_source
    soup=bs.BeautifulSoup(page,"lxml")
    for size in soup.find_all('a',class_="chAccount"):
        print(size.text)
    ''' cookies_=driver.get_cookies()
    print(cookies_) '''
    
    ''' with requests.session() as c:
        headers={
            'Referer':'https://configurx.it.abb.com/CXEngineX/content/jModelList.aspx',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Cookie':'_ga=GA1.2.952949306.1573200937; IsInsidePlusUser=1; _gid=GA1.2.1233880767.1575343347; ASP.NET_SessionId=1b24shj2ztscgzzne5pgr1gm',
        }
        filter_result=c.get("https://configurx.it.abb.com/CXEngineX/Content/JModelConfiguration.aspx",headers=headers,verify=False)
        #print(filter_result.text)
        soups=bs.BeautifulSoup(filter_result.text,"lxml")
        for h in soups.find_all('a',class_="chAccount"):
            print(h.text) '''
    
    time.sleep(1)
    driver.find_element_by_xpath("//select[@id='TabMasterContent_ddl_1']@data-digits="[3587803]"").click()
    driver.find_element_by_link_text("H : Hard Rubber").click()
    time.sleep(1)
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='H'])[1]/following::td[1]").click()
    driver.find_element_by_link_text("1 : Standard").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Lead Time'])[1]/following::td[2]").click()
    driver.find_element_by_link_text("S : Stainless steel 316").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='S'])[1]/following::td[1]").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Grounding Accessories'])[1]/following::a[1]").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Standard'])[1]/following::td[10]").click()
    driver.find_element_by_link_text("C2 : Flanges AWWA C207 Class D").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='A1'])[1]/following::td[1]").click()
    driver.find_element_by_link_text("B : Carbon steel").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='B'])[1]/following::td[1]").click()
    driver.find_element_by_link_text("1 : Standard (without PED)").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Lead Time'])[1]/following::td[2]").click()
    driver.find_element_by_id("totalContentWait").click()
    driver.find_element_by_link_text("A : Standard factory calibration").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='A'])[1]/following::td[1]").click()
    driver.find_element_by_link_text(u"1 : Standard design / -20 ... 60 °C (-4 ... 140 °F)").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Lead Time'])[1]/following::td[2]").click()
    driver.find_element_by_link_text("A : Adhesive label").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='A'])[1]/following::td[1]").click()
    driver.find_element_by_link_text("0 : Without signal cable").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Lead Time'])[1]/following::td[2]").click()
    driver.find_element_by_link_text("P : usFMc Div. 2").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='P'])[1]/following::td[1]").click()
    driver.find_element_by_link_text("1 : IP 67 (NEMA 4X) / IP 67 (NEMA 4X), integral").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Lead Time'])[1]/following::td[2]").click()
    driver.find_element_by_link_text("B : NPT 1/2 in.").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='B'])[1]/following::td[1]").click()
    driver.find_element_by_link_text("3 : 100 ... 230 V AC, 60 Hz").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Lead Time'])[1]/following::td[12]").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Input and Output Signal Type'])[1]/following::a[1]").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='A'])[1]/following::td[1]").click()
    driver.find_element_by_link_text("1 : Parameters set to factory defaults / Standard diagnostic").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Lead Time'])[1]/following::td[2]").click()
    driver.find_element_by_id("Header_cmdSave").click()
    driver.find_element_by_id("Cntnt_lbExportToExcel").click()
if __name__ == "__main__":
    login()
    filtercode()
    code_selection()
    driver.close()


""" class cx(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_123(self):
        driver = self.driver
        driver.get("https://configurx.it.abb.com/configurx/")
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("txtLogin").clear()
        driver.find_element_by_id("txtLogin").send_keys("Thomas-tao.wang@cn.abb.com")
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("System02")
        driver.find_element_by_id("cmdLogin").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("x1x1").click()
        driver.find_element_by_id("x1x1x1").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=2 | ]]
        driver.find_element_by_id("cboMarket").click()
        Select(driver.find_element_by_id("cboMarket")).select_by_visible_text("(USD) USA")
        driver.find_element_by_id("cboMarket").click()
        driver.find_element_by_id("cmdBasket").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("Cntnt_txtFilterCode").click()
        driver.find_element_by_id("Cntnt_txtFilterCode").clear()
        driver.find_element_by_id("Cntnt_txtFilterCode").send_keys("FEW315")
        driver.find_element_by_id("Cntnt_cmdFilter").click()
        driver.find_element_by_link_text("FEW315_C").click()
        driver.find_element_by_link_text("100 : DN 100 (4 in.)").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='DN 80 (3 in.)'])[1]/following::td[5]").click()
        driver.find_element_by_link_text("H : Hard rubber").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='H'])[1]/following::td[1]").click()
        driver.find_element_by_link_text("1 : Standard").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Lead Time'])[1]/following::td[2]").click()
        driver.find_element_by_link_text("S : Stainless steel 316").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='S'])[1]/following::td[1]").click()
        driver.find_element_by_link_text("4 : 2x Potential Equalizing Rings (Stainless Steel)").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Standard'])[1]/following::td[10]").click()
        driver.find_element_by_link_text("A1 : Flanges ANSI / ASME B16.5 / 16.47 series B Class 150").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='A1'])[1]/following::td[1]").click()
        driver.find_element_by_id("contentRegionPopup").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='B'])[1]/following::td[1]").click()
        driver.find_element_by_link_text("1 : Standard (without PED)").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Lead Time'])[1]/following::td[2]").click()
        driver.find_element_by_link_text("A : Standard factory calibration").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='A'])[1]/following::td[1]").click()
        driver.find_element_by_link_text(u"1 : Standard design / -20 ... 60 °C (-4 ... 140 °F)").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Lead Time'])[1]/following::td[2]").click()
        driver.find_element_by_link_text("A : Adhesive label").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='A'])[1]/following::td[1]").click()
        driver.find_element_by_link_text("0 : Without signal cable").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Lead Time'])[1]/following::td[2]").click()
        driver.find_element_by_link_text("P : usFMc Div. 2").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='P'])[1]/following::td[1]").click()
        driver.find_element_by_link_text("1 : IP 67 (NEMA 4X) / IP 67 (NEMA 4X), integral").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Lead Time'])[1]/following::td[2]").click()
        driver.find_element_by_link_text("B : NPT 1/2 in.").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='B'])[1]/following::td[1]").click()
        driver.find_element_by_link_text("3 : 100 ... 230 V AC, 60 Hz").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Lead Time'])[1]/following::td[12]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Input and Output Signal Type'])[1]/following::a[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='A'])[1]/following::td[1]").click()
        driver.find_element_by_link_text("1 : Parameters set to factory defaults / Standard diagnostic").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Lead Time'])[1]/following::td[2]").click()
        driver.find_element_by_id("Header_cmdSave").click()
        driver.find_element_by_id("Cntnt_lbExportToExcel").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main() """
