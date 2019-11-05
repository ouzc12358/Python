import requests as re

def getHTMLTEXT(url):
    try:
        r = re.get(url,timeout=30)
        r.raise_for_status()
       # print(r.raise_for_status)
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "ERROR"

if __name__=="__main__":
    url="http://192.168.1.1/index_status_userInfo.html"
    print(getHTMLTEXT(url)) 
 
