src=['A','B','C','D']  
des=['B','C','D','A']  
d1=len(src)  
d2=len(des)  
#print((d1,d2))  
def match():  
    for i in range(d1):  
        if des[0]==src[i]:  
            for j in range(1,d2):  
                if des[j]!=src[(i+j)%d1]:  
                    break  
            else:  
                #loop complete with finding a match  
                return True  
        else:  
            return False  
