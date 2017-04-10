n=raw_input()
num=map(int,raw_input().split())
minnum=min(num)
maxnum=max(num)
early=[]
k=0
for x in range(minnum,maxnum+1):
    early.append(x)
for i in range(len(early)):
    if early[i] not in num:
        k=k+1
        pro=early[i]
if k>1:
    print 'mistake'
elif k==1:
    print pro
elif k==0:
    if minnum==1:
        print maxnum+1
    else:
        print minnum-1,maxnum+1
