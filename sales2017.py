import pandas
import numpy
F = "FEW-CN"
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

col_name = sales_2017.columns.tolist()
print(col_name)
type_column = []
print(type_column)
for c in col_name:
    if c is F:
       type_column.append(c)
typeofEMF = sales_2017[type_column]
print(type_column.append(c))
print(typeofEMF)
print(typeofEMF.head(3))