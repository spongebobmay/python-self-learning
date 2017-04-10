newsize=raw_input("")
fishnumber=raw_input("")
fishsize=raw_input("")
fishs=fishsize.split(' ')
fishslist=list(set(map(int,fishs)))
minsize=int(newsize.split(' ')[0])
maxsize=int(newsize.split(' ')[1])
sort=0
w=[]
size=minsize
while size<=maxsize:
    for present_fish in fishslist:
        if  2*size<=present_fish<=10*size or 2*present_fish<=size<=10*present_fish:
            w.append(size)
    size+=1
finalsort=maxsize-minsize+1-len(set(w))
print finalsort
