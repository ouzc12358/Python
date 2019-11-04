import datetime as dt
import matplotlib.pyplot as plt
from   matplotlib import style
import pandas as pd 
import pandas_datareader.data as web

style.use ('ggplot')

""" start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)

df =  web.DataReader('TSLA','yahoo',start,end)
df.to_csv('tsla.csv') """

#df =pd.read_excel('order.xlsx', index_col= 'Creation Date')
df =pd.read_csv('tsla.csv',index_col = 0)

#print(df)
#usorder = df[["TYPE","Material sales text","Net value","Quantity"]]
""" print(usorder)
usorder.to_csv('usorder.csv') """


df['100ma']= df['Adj Close'].rolling(window=100,min_periods=0).mean()

#print(df)

#df.to_csv('tsla1.csv')

#usorder['average']
ax1= plt.subplot2grid((500,1),(0,0),rowspan=5,colspan=1)
#print(ax1)
ax2= plt.subplot2grid((500,1),(400,0),rowspan=1,colspan=1,sharex=ax1)
#ax1.plot(usorder.index,usorder['Net value'])
ax1.plot(df.index,df['Adj Close'])
ax1.plot(df.index,df['100ma'])
ax2.bar(df.index,df['Volume'])
#df['Net value'].plot()
plt.show()

""" df['Adj Close'].plot()
plt.show() """