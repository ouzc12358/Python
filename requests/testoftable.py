#a = "FEW315.025.A.1.S.1.A1.B.1.A.1.A.0.P.1.B.3.A.1.M5-V3.CWY"
#b= 'FEW315.025.A.1.S.1.A1.B.1.A.1.A.0.P.1.B.3.A.1.M5-V3.CWY'
b=input("code:")
def clean_mark(s):
    s=s.replace('.','')
    s=s.replace('-','')
    return s 
a = clean_mark(b)
  
maincode = a[0:6]
size = a[6:9]
letter = a[9:27]
language = a[27:29]
verification = a[29:31]
certificate =a[31:34]

print(maincode)

size = int(size)
print(size)

