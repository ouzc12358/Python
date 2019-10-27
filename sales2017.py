import pandas
import numpy
#orders=r"order.xlsx"
sales_2017 =pandas.read_excel("order.xlsx")
print (type(sales_2017))
#print(sales_2017.dtypes)
#print(sales_2017)
#print(sales_2017.head(300))
#print(sales_2017.tail(50))
print(sales_2017.columns)
print(sales_2017.shape)
#print(sales_2017.loc[10:30])
SO = sales_2017["Sales Orde"]
print(SO)
column = ["Sales Orde","Quantity"]
order_qty = sales_2017[column]
print(order_qty)