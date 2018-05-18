#最长回文字串，manacher算法实现，python2.7版本
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    slist='#'.join(s)
    slist= '#'+slist+'#'
    #以#字符填充字符
    index=-1
    pR=-1
    maxR=0
    pArr=[0 for i in xrange(len(slist))]
    for i in xrange(len(slist)):
        pArr[i]=min(pArr[2*index-i],pR-i) if pR>i else  1
        while i+pArr[i]<len(slist) and i-pArr[i]>-1:
            if slist[i+pArr[i]]==slist[i-pArr[i]]:
                pArr[i]+=1
            else:
                break
        if i+pArr[i]>pR:
            pR= i+pArr[i]
            index=i;
        maxR = max(pArr[i],maxR)
    return maxR-1
print longestPalindrome("aabbac")
#输出7

