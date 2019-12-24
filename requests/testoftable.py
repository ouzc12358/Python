#a = "FEW315.025.A.1.S.1.A1.B.1.A.1.A.0.P.1.B.3.A.1.M5-V3.CWY"
#b= 'FEW315.750.H.1.S.1.A1.B.1.A.1.A.0.P.1.B.3.A.1.M5-V3.CWY'
#b= 'FEW315.801.H.1.S.1.A1.B.1.A.1.A.0.P.1.B.3.A.1.M5-V3.CWY'
#b= 'FEW315.801.K.1.D.1.A1.B.1.A.1.A.0.P.1.B.3.A.1.M5-V3.CWY'
#b= 'FEW315.750.H.1.S.1.A1.B.1.A.1.A.0.P.1.B.3.A.1.M5-V3.CWY'
''' b=input("code:")
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
 '''
''' _size_ = [700,
750,
800,
900,
1000,
1050,
1100,
1200,
1350,
1400,
1500,
1600,
1650,
1800,
1950,
2000,
2100,
2200,
2400
]
i=0 '''
#print(_size_[i])
''' for i in range(len(_size_)):
    if _size_[i]==2200:
        size =_size_[i]+50
    else:
        size = _size_[i]+15
    b=-0.000002*pow(size,2) + 0.0164*size - 8.2093
    b=round(b)
    print(b)
    i=i+1 '''
c = 2100
i=0
''' c = c+50
def NodeTransformer(select):
    d= -0.000002*pow(c,2) + 0.0164*c - 8.2093
    d=round(d)
    print(d)
    d= str(d)
    select = "chRow:nth-child("+d+") .chC2p"
    #print(select)
    return select
x = NodeTransformer(c)
print(x)
 '''

''' i = 0
   # return product,maincode,size,letter,
def transforomencoding(_size_):
    
    if _size_==2200:
        size =_size_+50
    else:
        size = _size_+15
    encode=-0.000002*pow(_size_,2) + 0.0164*_size_ - 8.2093
    encode = round(encode)
    select  =  str(encode)
    size_selection = ".chRow:nth-child("+select+") .chC2p"
    return size_selection '''
#return maincode,size,letter,language,verification,cer
''' def transforomencoding(_size_):
    if _size_==2200:
        size =_size_+50
    else:
        size = _size_+15
    encode=-0.000002*pow(_size_,2) + 0.0164*_size_ - 8.2093
    encode = round(encode)
    select  =  str(encode)
    size = "chRow:nth-child("+select+") .chC2p"
    return size
c = transforomencoding(c)
print(c) '''

def transformsize(_size):
    if _size%10 == 0:
        encode = 0.0149*_size-8.2
        encode = round(encode)
        _tmp = str(encode)
        _sizecode = "chRow:nth-child("+_tmp+") .chC2p"
    elif _size == 651:
        _sizecode = "chRow:nth-child(14) .chC2p"
    else:
        encode = 0.011*_size+6.4755
        encode = round(encode)
        _tmp = str(encode)
        _sizecode = "chRow:nth-child("+_tmp+") .chC2p"
    return _sizecode

a = 801

b= transformsize(a)
print(b)  
