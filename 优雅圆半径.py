import math
rsqrt=raw_input("")
rs=int(rsqrt)
k=0
i=0
while(i<math.sqrt(rs)):
    j=int(math.sqrt(rs-i*i))
    if (i*i+j*j)==rs:
        k+=1
    i+=1
print k*4
