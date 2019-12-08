import bs4 as bs
import requests as re
import urllib3
from selenium import webdriver
import pickle
from selenium.webdriver.chrome.options import Options
##import json
#import dryscrape

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # remove "InsecureRequestWarning" meassage

with re.session() as c:  
    url = "https://configurx.it.abb.com/configurx/content/Login.aspx"
    Logged_url="https://configurx.it.abb.com/configurx/content/Logged.aspx"
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Referer':'https://configurx.it.abb.com/configurx/content/Login.aspx'
    }
    data = {
        '__VIEWSTATE': '/wEPDwUKMTkwMDA0NDE2NQ9kFgICAQ9kFjQCAQ8PFgIeBFRleHQFFFdlbGNvbWUgaW4gQ29uZmlndXJYZGQCAw8PFgIfAAULSU5GT1JNQVRJT05kZAIFDw8WAh8ABQhFLW1haWw6IGRkAgcPDxYEHwAFC0luZm9ybWF0aW9uHgtOYXZpZ2F0ZVVybAVQbWFpbHRvOmluc3RydW1lbnRhdGlvbnguc3VwcG9ydEBpdC5hYmIuY29tP3N1YmplY3Q9SW5zdHJ1bWVudGF0aW9uWDogSU5GT1JNQVRJT05kZAIJDw8WAh8ABQVUZWw6IGRkAgsPDxYCHwAFAzAwMGRkAg0PDxYCHwAFEVRFQ0hOSUNBTCBTVVBQT1JUZGQCDw8PFgIfAAUIRS1tYWlsOiBkZAIRDw8WBB8ABQlTdXBwb3J0DQofAQVWbWFpbHRvOmluc3RydW1lbnRhdGlvbnguc3VwcG9ydEBpdC5hYmIuY29tP3N1YmplY3Q9SW5zdHJ1bWVudGF0aW9uWDogVEVDSE5JQ0FMIFNVUFBPUlRkZAITDw8WAh8ABQVUZWw6IGRkAhUPDxYCHwAFAzAwMGRkAhcPDxYCHwAFB1JFTEVBU0VkZAIZDw8WAh8ABR8xMC40NTIuMCByZWxlYXNlZCBvbjExIE9jdCAyMDE5ZGQCHQ8PFgIfAAUNQUJCIENPTkZJR1VSWGRkAh8PDxYCHwAF/wE8Yj5Db25maWd1clg8L2I+IGlzIGFuIEludGVybmV0LWJhc2VkIGFwcGxpY2F0aW9uIHdoaWNoIHByb3ZpZGUgYXV0aG9yaXplZCB1c2VycyB3aXRoIGEgcG93ZXJmdWwgcHJvZHVjdCBjb25maWd1cmF0aW9uIGVudmlyb25tZW50Ljxicj5JdGBzIHBhcnQgb2YgdGhlIEluc3RydW1lbnRhdGlvblggU3VpdGUgYW5kIHdvcmtzIGluIGRpcmVjdCBjb25uZWN0aW9uIHdpdGggdGhlIEluc3RydW1lbnRhdGlvblggUHJvZHVjdCBHbG9iYWwgQ29udGVudC5kZAIhDw8WAh8ABRVMT0dJTiBJTlRPIFRIRSBTWVNURU1kZAIjDw8WBB8AZR4HVmlzaWJsZWhkZAIkDw8WBB8AZR8CaGRkAiYPDxYCHwAFC1VzZXIgTmFtZTogZGQCKg8PFgIfAAUKUGFzc3dvcmQ6IGRkAi4PDxYCHwAFBUxvZ2luZGQCMA8WAh8CaBYEZg9kFgJmDw8WAh8ABQhNYXJrZXQ6IGRkAgEPZBYCZg8QZGQWAGQCMg8PFgIfAAUrVXNlciBOYW1lIGFuZCBQYXNzd29yZCBhcmUgY2FzZSBzZW5zaXN0aXZlLmRkAjQPDxYCHwAFHURJRCBZT1UgRk9SR0VUIFlPVVIgUEFTU1dPUkQ/ZGQCOg8PFgIfAAUEU2VuZGRkAjwPDxYCHwAFc1BsZWFzZSBpbnNlcnQgeW91ciBVc2VyIEUtbWFpbCBhZGRyZXNzLjxicj5Vc2VyIE5hbWUgYW5kIFBhc3N3b3JkIHdpbGwgYmUgc2VudCBhdXRvbWF0aWNhbGx5IHRvIHlvdXIgdHlwZWQgYWRkcmVzcy5kZGSeWqHrF3jeTtVW7gAs8VhBPQ3CmkO7PlylFkUwqqX0vQ==',
        '__VIEWSTATEGENERATOR':'9CA0CFBB',
        '__EVENTVALIDATION':' /wEdAAaSJ11LiwK3vAQYySWybSavxcn6oIDdbNQI5AQUIIyv4nY2+Mc6SrnAqio3oCKbxYaKVZBXgGQ/GUR0UoSGGFdN8lcVMzLLXeEaNXy6K7qCcqKah4gBOJF3lXZOOLxfjvX8yvBW07V17BWBRAhRmjm3xCzClcBcwsw2otVwFwQ2aw==',
        'txtLogin':' Thomas-tao.wang@cn.abb.com',
        'txtPassword':' System02',
        'cmdLogin':' Login',
        'txtEmail3':' '
    } # the data that we all need is here, when the password changed, please update your password.
    #res=c.get(url,verify=False,headers = headers)
    resp= c.post(url,data=data,headers = headers,verify=False)
    Logged_cx= c.get(Logged_url,verify=False)
    #print(Logged_cx.text) # verify if logged in successful or not, from feedback text and know it works, so do not need to run again 
    menu_url='https://configurx.it.abb.com/configurx/content/DetailPopupBasket.aspx?CONF=1'
    market_select={
        '__EVENTTARGET':' cboMarket',
        '__EVENTARGUMENT':' ',
        '__LASTFOCUS':' ',
        '__VIEWSTATE':' /wEPDwUKLTE1MjIzNTg3OQ9kFgICAQ9kFhoCAQ9kFgQCAQ8PFgIeBFRleHQFqAFXZWxjb21lJm5ic3A7PEI+dGhvbWFzLXRhby53YW5nQGNuLmFiYi5jb208L0I+LiBZb3VyIGxhc3QgbG9naW4gaXMmbmJzcDs8Qj4wMS8xMi8yMDE5PC9CPiBhdCZuYnNwOzxCPjA1OjQ0OjM3PC9CPiAtICZuYnNwOzxCPkNOQVVTPC9CPiAtIFJFTEVBU0U6Jm5ic3A7PEI+MTAuNDUyLjAuNDwvQj5kZAIDDxYCHgdWaXNpYmxlaBYCZg9kFgICAQ8PFgIfAGVkZAIDDw8WAh8ABQlDb25maWd1clhkZAIFDw8WAh8ABQtGSUxURVIgTElTVGRkAgcPDxYCHwAFB01hcmtldDpkZAIJDxBkEBWOAQhTZWxlY3QuLhVHbG9iYWwgQ29udGVudCBNYXJrZXQNKFVTRCkgQWxiYW5pYQ0oVVNEKSBBbGdlcmlhDChVU0QpIEFuZ29sYQ8oVVNEKSBBcmdlbnRpbmEPKFVTRCkgQXVzdHJhbGlhDShVU0QpIEF1c3RyaWEQKFVTRCkgQXplcmJhaWphbg0oVVNEKSBCYWhyYWluEChVU0QpIEJhbmdsYWRlc2gNKFVTRCkgQmVsYXJ1cxooVVNEKSBCZWxhcnVzIEVuZXJnb3Byb21pcw0oRVVSKSBCZWxnaXVtCyhVU0QpIEJlbmluDShVU0QpIEJvbGl2aWESKFVTRCkgQm9zbmlhLUhlcnouDihVU0QpIEJvdHN3YW5hDChVU0QpIEJyYXppbA4oVVNEKSBCdWxnYXJpYQ4oVVNEKSBDYW1lcm9vbgwoVVNEKSBDQU5BREELKFVTRCkgQ2hpbGULKENOWSkgQ2hpbmEbKFVTRCkgQ2hpbmEgZmFjdG9yeSBVU0QgUExTDChDTlkpIENoaW5hMg4oVVNEKSBDb2xvbWJpYQsoVVNEKSBDb25nbw0oVVNEKSBDcm9hdGlhDChVU0QpIEN5cHJ1cxAoVVNEKSBDemVjaCBSZXAuDihFVVIpIERFRXhwb3J0CihVU0QpIERlbW8NKFVTRCkgRGVubWFyaxEoVVNEKSBERVByb2NBdXRvbQ8oVVNEKSBERVNlcnZpY2URKFVTRCkgREVVdGlsQXV0b20NKFVTRCkgRWN1YWRvcgsoVVNEKSBFZ3lwdBkoVVNEKSBFZ3lwdCBUdXJib2NoYXJnZXJzDShVU0QpIEVyaXRyZWENKFVTRCkgRXN0b25pYQ4oVVNEKSBFdGhpb3BpYQ0oVVNEKSBGaW5sYW5kDChFVVIpIEZyYW5jZQsoVVNEKSBHYWJvbg0oRVVSKSBHZXJtYW55CyhVU0QpIEdoYW5hEyhVU0QpIEdyZWF0IEJyaXRhaW4MKFVTRCkgR3JlZWNlDyhVU0QpIEhvbmcgS29uZw0oVVNEKSBIdW5nYXJ5DShVU0QpIEljZWxhbmQLKFVTRCkgSW5kaWEPKFVTRCkgSW5kb25lc2lhCihFVVIpIElyYW4KKFVTRCkgSXJhcQ0oVVNEKSBJcmVsYW5kDChVU0QpIElzcmFlbA8oVVNEKSBJc3JhZWwgRlAWKFVTRCkgSVQgTGFyZ2UgcHJvamVjdA0oVVNEKSBJVCBURU1BCyhVU0QpIEl0YWx5DShVU0QpIElUV2F0ZXIRKFVTRCkgSXZvcnkgQ29hc3QLKFVTRCkgSmFwYW4MKFVTRCkgSm9yZGFuEChVU0QpIEthemFraHN0YW4LKFVTRCkgS2VueWEMKFVTRCkgS3V3YWl0DChFVVIpIExhdHZpYQ0oVVNEKSBMZWJhbm9uCyhVU0QpIExpYnlhDyhVU0QpIExpdGh1YW5pYRAoRVVSKSBMdXhlbWJvdXJnDyhVU0QpIE1hY2Vkb25pYRAoVVNEKSBNYWRhZ2FzY2FyDihVU0QpIE1hbGF5c2lhCihVU0QpIE1hbGkLKFVTRCkgTWFsdGEPKFVTRCkgTWF1cml0aXVzDChVU0QpIE1leGljbwwoVVNEKSBNb25hY28NKFVTRCkgTW9yb2NjbxEoRVVSKSBOZXRoZXJsYW5kcxEoVVNEKSBOZXcgWmVhbGFuZA0oVVNEKSBOaWdlcmlhEShVU0QpIE5vcnRoIEtvcmVhDChVU0QpIE5vcndheQooVVNEKSBPbWFuDihVU0QpIFBha2lzdGFuDShVU0QpIFBhbmFtw6AKKFVTRCkgUGVydREoVVNEKSBQaGlsaXBwaW5lcwwoVVNEKSBQb2xhbmQOKFVTRCkgUG9ydHVnYWwLKFVTRCkgUWF0YXINKFVTRCkgUm9tYW5pYR0oVVNEKSBSdXNzaWEgQ2hhbm5lbCBQYXJ0bmVycxIoRVVSKSBSdXNzaWFuIEZlZC4SKFVTRCkgU2F1ZGkgQXJhYmlhIyhVU0QpIFNhdWRpIEFyYWJpYSBDaGFubmVsIFBhcnRuZXJzDShVU0QpIFNlbmVnYWwMKFVTRCkgU2VyYmlhEihVU0QpIFNpZXJyYSBMZW9uZQ8oVVNEKSBTaW5nYXBvcmUOKFVTRCkgU2xvdmFraWEOKFVTRCkgU2xvdmVuaWESKFVTRCkgU291dGggQWZyaWNhIyhVU0QpIFNvdXRoIEFmcmljYSBDaGFubmVsIFBhcnRuZXJzEShVU0QpIFNvdXRoIEtvcmVhCyhVU0QpIFNwYWluDyhVU0QpIFNyaSBMYW5rYQsoVVNEKSBTdWRhbgwoVVNEKSBTd2VkZW4RKFVTRCkgU3dpdHplcmxhbmQLKFVTRCkgU3lyaWEMKFVTRCkgVGFpd2FuDihVU0QpIFRhbnphbmlhDihVU0QpIFRoYWlsYW5kCihVU0QpIFRvZ28NKFVTRCkgVHVuaXNpYQwoVVNEKSBUdXJrZXkNKFVTRCkgVWtyYWluZRUoVVNEKSBVbml0LkFyYWIgRW1pci4XKFVTRCkgVW5pdC5BcmFiIEVtaXIuIDIXKFVTRCkgVW5pdC5BcmFiIEVtaXIuIDMNKFVTRCkgVXJ1Z3VheQkoVVNEKSBVU0EQKFVTRCkgVXpiZWtpc3Rhbg8oVVNEKSBWZW5lenVlbGENKFVTRCkgVmlldG5hbQsoVVNEKSBZZW1lbhAoVVNEKSBZdWdvc2xhdmlhEyhFVVIpIFoxIEFCQiBNYXJpbmUaKFVTRCkgWjEgQUJCIFBvd2VyIFN5c3RlbXMOKFVTRCkgWmltYmFid2UhKFVTRCkgWlogR2xvYmFsIEZyYW1lIEFnciBBY2Npb25hIihFVVIpIFpaIEdsb2JhbCBGcmFtZSBBZ3IgQkFTRl8iQiIiKEVVUikgWlogR2xvYmFsIEZyYW1lIEFnciBCQVNGXyJDIiMoRVVSKSBaWiBHbG9iYWwgRnJhbWUgQWdyIEVuZ2llIEVVUiMoVVNEKSBaWiBHbG9iYWwgRnJhbWUgQWdyIEVuZ2llIFVTRBWOAQABMAMxMDUCNDMCNTICMTUCMzkBNAMxMTMCNzYCMzQDMTE3AzIxMwI4NAI1MwIyMAMxMDMCNTQCMTQDMTAxAjQ0AjE5AjIxAjI5AzIyNgMyMzQCMjICNDUDMTAyAzEwMAI5MQMyMDIDMTEyATUDMjA0AzIwMwMyMDUCMjMCNjgDMjQ0AjU1Ajk3AjU2ATcCODYCNTcBMgI0NgEzAjk4AjMwAjkzAjEwAjM1AjQwAzEyMQI2OQI4OQI2NwMyMTEDMjMxAzI0OQExAzIwNwI0NwIzMQI3MAMxMTgCNTgCNzcCOTUCNzECNzICOTQCMTEDMjI4AjU5AjM2AjQ4AjczAjYwAjE2AjEyAjQ5Ajg1AjQxAjYxAjMyATgCNzgCNzkDMTE0AjI0AjI3AjkwAjEzAjgwAzEwOAMyMjcDMTA3AjgxAzI2MgI1MAMxMTUCNjICNDICOTIDMTA0Ajc0AzI0OAIzMwI4NwIzNwI2MwE5ATYCNzUCMjgCNjQCMzgCNjUCNTECOTkCOTYCODIDMjY1AzI2NgIxOAIyNgMxMTkCMjUDMTE2AjgzAzEwNgMyNDMDMjI1AjY2AzI2NwMyMzUDMjQ3AzI0MQMyNDIUKwOOAWdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dkZAILDw8WAh8ABQhDYXRhbG9nOmRkAg0PEGQQFRMEMjAyMAQyMDE5BDIwMTgEMjAxNwQyMDE2BDIwMTUEMjAxNAQyMDEzBDIwMTIEMjAxMQQyMDEwBDIwMDkEMjAwOAQyMDA3BDIwMDYFMjAwNSAEMjAwNAQyMDAyBDIwMDEVEwIyMAIxOQIxOAIxNwIxNgIxNQIxNAIxMwIxMgIxMQIxMAE5ATgBNwE2ATUBNAExATIUKwMTZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAg8PDxYCHwAFCUxhbmd1YWdlOmRkAhEPEGQQFQ0IU2VsZWN0Li4HQ2hpbmVzZQZEYW5pc2gHRGV1dHNjaAVEdXRjaAdFbmdsaXNoB0VzcGFub2wHRmlubmlzaAhGcmFuY2FpcwhJdGFsaWFubwpQb3J0b2d1ZXNlB1J1c3NpYW4HU3dlZGlzaBUNAAIxMAIxMQEzATcBMgE1AjEyATQBMQIxNQIxMwIxNBQrAw1nZ2dnZ2dnZ2dnZ2dnZGQCEw8WAh8BaBYEZg9kFgICAQ8PFgIfAAURU2VsbGluZyBjdXJyZW5jeTpkZAIBD2QWAgIBDxBkZBYAZAIVDw8WBB8ABQxEaXJlY3QgaW5wdXQeB0VuYWJsZWRoZGQCFw8PFgQfAAUMQ29uZmlndXJhdG9yHwJoZGQCGQ8PFgQfAAUUTWFya2V0IG5vdCBzZWxlY3RlZCEfAWdkZGSCst8oThNy7aaBo8oeLrhffTGBYF20BrLa3cNHQJz/uQ==',
        '__VIEWSTATEGENERATOR':' 4F83A1DB',
        '__EVENTVALIDATION':' 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',
        'cboMarket':' 26',
        'cboCatalog':' 19',
        'cboDocumentLanguageID':' 2',
    }
    market_headers= {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Referer':'https://configurx.it.abb.com/configurx/content/DetailPopupBasket.aspx?CONF=1'
               
    }
    c.post(menu_url,data=market_select,headers=market_headers) # post the market select to site.
    market_result=c.get(menu_url,verify=False)# get the market result and check if that works, if that works, we could see the market form and year form from terminal 
    #print(market_result.text)# it works and we could move forward

    #### after market selection, go to main configuratore.aspx
    filter_index_url="https://configurx.it.abb.com/CXEngineX/Index.aspx"
    index_data={
        'ConfigRequest':'<?xml version="1.0" encoding="utf-8"?><ApplicationRequest><ApplicationDetail><Application>CX</Application><CurrentCulture>it-IT</CurrentCulture><DateFormat>dd/MM/yyyy</DateFormat><GUILanguageID>2</GUILanguageID><HTTPAdressDocumentationCID>https://library.abb.com/share?cid=</HTTPAdressDocumentationCID><UserTipology>FF</UserTipology><HookUrl>https://configurx.it.abb.com/configurx/content/ConfiguratorX.aspx</HookUrl><WsIXB2BUrl></WsIXB2BUrl></ApplicationDetail><SessionDetail><MarketId>26</MarketId><CatalogId>19</CatalogId><IdDestinationMarket>26</IdDestinationMarket><DocumentLanguageId>2</DocumentLanguageId><ProducerCode>CNAUS</ProducerCode><SellingCurrency></SellingCurrency><TypeUser></TypeUser><IdUser>7389</IdUser><QueryStringACC></QueryStringACC><QueryStringMOD></QueryStringMOD><QueryStringTYP></QueryStringTYP><CurrencyDecimals>2</CurrencyDecimals><ConversionRate>1</ConversionRate><UserDescription>thomas-tao.wang@cn.abb.com</UserDescription><MarketDescription>USA[US]</MarketDescription><CatalogueDescription>2019</CatalogueDescription><TestAmbientDescription></TestAmbientDescription><IDDocument>0</IDDocument><IDX></IDX><Cart_CodForn></Cart_CodForn><Cart_Discount></Cart_Discount><Cart_CodeIndex></Cart_CodeIndex><ParametersMode></ParametersMode></SessionDetail></ApplicationRequest>'
    }
    c.post(filter_index_url,data=index_data,verify=False)#when the browser jump to new window, there have an index need to post the jump data to server, then the server will return the right value of page, including the username , market selection etc information are expected by server.
    filter_Configurator_url="https://configurx.it.abb.com/CXEngineX/content/jModelList.aspx"# the page when we jump into and configure the code selection
    usa_result=c.get(filter_Configurator_url,verify=False)# test if the code works, and ask the source code of site.
    print(usa_result.text) # turn out to be works, return the right value
    #========================= use selenium module to excute code and got the dynamic page data
    ''' print(c.cookies)
    #driver = webdriver.Chrome()
    cookies_s=[
        {    'name': cookie.name, 'value': cookie.value, 'domain': cookie.domain, 'path': cookie.path    }
        for cookie in c.cookies
    ] '''
    
  
    ''' header_cookies = ";".join([item["name"] + "=" + item["value"] + "" for item in cookies_s])
    hearders={
        'Cookie':header_cookies
    }
    test1=c.get(filter_Configurator_url,headers=header_cookies)
    print(test1)
     '''
    ''' driver = webdriver.Chrome()

    for item in cookies_s:
        driver.add_cookie(
            {
                'domain':item['domain'],
                'name':item['name'],
                'value':item['value'],
                'path':item['path'],
                'secure': True,
                'httpOnly': True, 
                
            }
        )
    driver.get(filter_Configurator_url)
    test_cookie=driver.get_cookies()
    print(test_cookie) '''
    ''' driver = webdriver.Chrome()
    cookie = driver.get_cookies()
    jsonCookies = json.dumps(cookie)
    cookies = pickle.load(open("cookies.txt", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    
    driver.get("https://configurx.it.abb.com/configurx/content/mainConfiguratore.aspx")
    
    get_filter_page= driver.execute_script("return document.documentElement.outerHTML")
    #driver.quit()
    soup= bs.BeautifulSoup(get_filter_page,"lxml")

    box=soup.find('div',id="Cntnt_lblFilterCode")
    #print(box) '''

    ''' maincode_url="https://configurx.it.abb.com/CXEngineX/WSModelList.asmx/WSFilters"
    maincode_headers={
        'Referer':'https://configurx.it.abb.com/CXEngineX/content/jModelList.aspx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    maincode_data = {"filterCode": "FEW315", "filterDescription": "", "cboTypeValue": "0", "currentPage": "1", "rowsForPage": "20" 
    }
    c.post(maincode_url,data=maincode_data,headers=maincode_headers, verify = False) '''
    
    


    
"""     filter_Configurator_url="https://configurx.it.abb.com/CXEngineX/WSModelList.asmx/WSFilters"
    filter_data={
        'filterCode': "FEW311", 
        'filterDescription': "", 
        'cboTypeValue': "0",
        'currentPage': "1",
        'rowsForPage': "20"
    }
    filter_headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Referer':'https://configurx.it.abb.com/CXEngineX/content/jModelList.aspx',    
    }
    filter_result = c.post(filter_Configurator_url,data=filter_data,headers = filter_headers)
    print(filter_result.json)

 """
    #selection_url = "https://configurx.it.abb.com/CXEngineX/content/jModelList.aspx"
    #code_configurX = c.get(selection_url)
    #soup=bs.BeautifulSoup(code_configurX.text,"lxml")
    #print(soup.prettify) 
    #print(code_configurX.text)
"""     upload_url = "https://configurx.it.abb.com/CXEngineX/WSModelList.asmx/WSFilters"
    send_maincode= {
        'filterCode': "FEW311", 
        'filterDescription': "", 
        'cboTypeValue': "0",
        'currentPage': "1",
        'rowsForPage': "20"
    }
    code_select = c.post(upload_url,data=send_maincode)
    filterresult_url="https://configurx.it.abb.com/configurx/content/mainConfiguratore.aspx"
    filterresult=c.get(filterresult_url,verify=False)
    print(filterresult.text) """