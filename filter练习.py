def not_su(n):
   x=2
   while x<n:
      if n%x==0:
           return x
      x+=1
print filter(not_su,range(1,101))
