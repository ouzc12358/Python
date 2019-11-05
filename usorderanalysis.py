import datetime as dt
import matplotlib.pyplot as plt
from   matplotlib import style
import pandas as pd 
import pandas_datareader.data as web

style.use ('ggplot')
df =pd.read_excel('order.xlsx', index_col= 'Creation Date')
usorder = df[["TYPE","Material sales text","Net value","Quantity"]]
#print(usorder)
ax1= plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2= plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)
ax1.plot(usorder.index,usorder['Net value'])
ax2.bar(usorder.index, usorder['Quantity'])
plt.show()