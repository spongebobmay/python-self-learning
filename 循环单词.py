n=int(raw_input())
word=[]
for x in xrange(n):
    word.append(raw_input())
i=n-1
while i>=0:
    j=len(word)-1
    while j>=0:
        if j>=0 and i>j and sorted(word[i])==sorted(word[j]):
            for x in xrange(len(word[i])):
                if word[i][x:]+word[i][:x]==word[j]:
                    word.remove(word[j])
                    i-=1
                    break
        j-=1
    i-=1
print len(word)
