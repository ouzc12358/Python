import requests as re

''' def getHTMLTEXT(url):
    try:
        r = re.get(url,timeout=30)
        r.raise_for_status()
       # print(r.raise_for_status)
        r.encoding=r.apparent_encoding
        
        return r.text
    except:
        return "ERROR"

if __name__=="__main__":
    url="https://item.jd.com/1364161.html"
    print(getHTMLTEXT(url)) ''' 

url="https://www.amon.cn/dp/B01HIUTCA8/ref=lp_2155051_1_1?s=apparel&ie=UTF8&qid=1573136023&sr=1-1"
#故意设定错误网址测试excep语句
try:
    kv={'user-agent':'Mozilla/5.0'}
    r=re.get(url,headers=kv)
    r.raise_for_status
    r.encoding=r.apparent_encoding
    print(r.text[1000:2000])
    print(r.status_code)
   # print (r.headers)
except:
    print("got failure")

