interval=raw_input("")
a=interval.split(' ')[0]
b=interval.split(' ')[1]
c=interval.split(' ')[2]
j=0
i=int(a)
while i<=int(b):
    if i%int(c)==0:
        j+=1
    i+=1
print '%d' %j
