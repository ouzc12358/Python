import pandas as pd
import numpy as np
d = pd.Series(range(20))
#print(d)
#print(d.cumsum)

#a = np.arange(100).reshape(5,20)
#np.savetxt('a.csv', a, fmt='%d', delimiter=',')
#np.savetxt("a1.csv", a, fmt="%.2f", delimiter=',')

#b = np.loadtxt("a1.csv", dtype=np.int, delimiter= ',')
#print(b)

a =  np.arange(100).reshape(5,10,2)
#print(a)
#np.savetxt('a.csv', a, fmt='%d',delimiter=',')
a.tofile("b.dat",  format= '%d')
#c =  np.fromfile("b.dat", dtype=np.int)
c =  np.fromfile("b.dat", dtype=np.int).reshape(5,10,2)
print(c)
c.tofile("c1.csv", sep=" ", format= '%d' )

f= np.fromfile("order.xlsx", dtype=np.str)
print(f)