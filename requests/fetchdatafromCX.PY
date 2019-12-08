import bs4 as bs
from bs4 import BeautifulSoup
import requests as re
import pandas as pd
import numpy as np
from urllib.request import urlopen
from requests.auth import HTTPBasicAuth


#url = "https://configurx.it.abb.com/CXEngineX/WSConfigurator.asmx/WSGetDigits"
#url = 'https://configurx.it.abb.com/configurx/'
""" def get_data_CX():
    r= re.get(url, verify=False)
    cx_login = r.text
    soup = bs.BeautifulSoup(cx_login,"html.parser")
   # r=re.get(url,verify=False,auth=('Thomas-tao.wang@cn.abb.com','System02'))
    #rsp = urlopen(url)
    #html = rsp.read().decode('utf-8', 'ignore')
    #print(html)      
    print(soup.prettify)
#r = re.get('https://configurx.it.abb.com/configurx/content/mainConfiguratore.aspx')
    ''' soup = bs.BeautifulSoup(r.text, "lxml")
    table = soup.find('table', {'class': 'wikitable sortable'}) '''

#print(r.headers)

get_data_CX() """
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',}
def login_CX(txtLogin,txtPassword):
    url = "https://configurx.it.abb.com/configurx/content/Login.aspx"
   # posturl = re.get(url, verify=False)
    postdata = {
         "txtLogin": txtLogin,
         "txtPassword": txtPassword,
     }  
    responseRes =  re.post(url,data = postdata,verify = False)
    #contents = re.get("https://configurx.it.abb.com/configurx/html/content.htm", verify= False)
    #soup = bs.BeautifulSoup(contents.text,"html.parser")
    #markets = re.get("https://configurx.it.abb.com/configurx/content/DetailPopupBasket.aspx?CONF=1",verify=False)
    #soup = bs.BeautifulSoup(markets.text, 'html.parser')
    name_url= re.get(responseRes,verify=False )
    soup_name = bs.BeautifulSoup(name_url.text,"html.parser")
    print(soup_name.prettify)
    #print(soup.prettify)

if __name__ == "__main__":
   login_CX("Thomas-tao.wang@cn.abb.com","System02") 

