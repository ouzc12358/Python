import requests as re
import os

''' kv = {'Wd':'点胖子'}
r = re.get("https://www.baidu.com/s",params= kv)
print(r.status_code)
print(r.request.url)
print(len(r.text)) '''

path="C:/Pictures"
url="https://media.wired.com/photos/598e35994ab8482c0d6946e0/master/w_2560%2Cc_limit/phonepicutres-TA.jpg"
r =re.get(url)
print(r.status_code)
with open(path,'wb') as f:
    f.write(r.content)
f.close
