n=int(raw_input(""))
a=[]
zeronum=0
onenum=0
twonum=0
threenum=0
fournum=0
fivenum=0
for i in range(n):
    a.append(raw_input(""))
for i in range(n):
    for j in (len(a[i])):
        if int(a[i][j])==0:
            zeronum+=1
        elif int(a[i][j])==1:
            onenum+=1
        elif int(a[i][j])==2:
            twonum+=1
        elif int(a[i][j])==3:
            threenum+=1
        elif int(a[i][j])==4:
            fournum+=1
        elif int(a[i][j])==5:
            fivenum+=1
        else:
            pass
b=6*5*4*3*2*1
print b
