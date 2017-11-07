string = "Any good range function is going to need to know where it is and where to head next"
l=string.split(' ')
s=0
lrc=[]
for i in l:
    ls=l[s]
    lrc.append(ls[::-1])
    lrc.append(' ')
    s +=1
listReverse=''.join(lrc)
print(listReverse)
    
    
