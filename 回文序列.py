n=int(raw_input())
item=[int(x) for x in raw_input().strip().split(' ')]
def huiwen(item,head,tail):
    times=0
    left=item[head]
    right=item[tail]
    while(head<tail):
        if (left<right):
            head+=1
            left+=item[head]
            times+=1
            continue
        elif left>right:
            tail-=1
            right+=item[tail]
            times+=1
            continue
        elif left==right:
            head+=1
            tail-=1
            left=item[head]
            right=item[tail]
    return times
print huiwen(item,0,n-1)
