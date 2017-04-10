str1=raw_input("")
str2=raw_input("")
j=0
k=0
a=[]
for i in range(len(str1)):
    if str1[i]==str2[i] and str1[i]!=' ':
            j+=1
            a.append(j)
    else:
            j=0
            a.append(j)
print max(a)
