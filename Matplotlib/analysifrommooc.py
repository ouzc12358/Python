import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mt

mt.rcParams['font.family']='FangSong'
plt.plot([3,1,4,5,2])
plt.ylabel("grade")
plt.xlabel("时间")
plt.axis([-1,10,0,6]) # 坐标系的确定，顺序为先X 后Y
plt.savefig('test',dpi=1000) #png file
plt.show() # 显示出绘制的图形

#plt.subplot(行数量，列数量，当前的绘图区)
""" plt.subplot(3,2,4) #表示绘制一个图，共有3行两列，当前绘图发生于区域4
plt.subplot(321)
plt.show() """
#实例
""" def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

a = np.arange(0.0,5,0.02)

plt.subplot(211)
plt.plot(a,f(a))

plt.subplot(212)
#plt.plot(a,np.cos(2*np.pi*t), 'r--') #似乎课程代码错误
plt.show() """
#实例结束


#plt.plot(X轴的数据/列表/数组/可选，Y 轴的数据/列表/数组，控制曲线的的格式字符串/可选，第二组或者更多的（X,Y,控制曲线格式）)
#当绘制多条曲线时候， 各条曲线的X 不能忽略
""" 
a = np.arange(10,20,dtype=int)
plt.plot(a,a*1.5,a,a*2.5,a,a*3.5,a,a*4.5)
plt.show() """
