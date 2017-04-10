n=int(raw_input(""))
a=raw_input("").split(' ')
i=n-1
j=0
while i>=0:
    j=len(a)-2
    while j>=0:
        if i>j and (int(a[j])==int(a[i])):
            a.remove(a[j])
            i-=1
        j-=1
    i-=1
for x in a:
    print (x),
