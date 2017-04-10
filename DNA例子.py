zfc=raw_input("")
zfc1=zfc.split(' ')[0]
zfc2=zfc.split(' ')[1]
j=0
for i in range(len(zfc1)):
    if (zfc1[i]=='A' and zfc2[i]!='T') or (zfc1[i]=='T' and zfc2[i]!='A')or (zfc1[i]=='C' and zfc2[i]!='G')or (zfc1[i]=='G' and zfc2[i]!='C'):
        j+=1
print '%d' %j
