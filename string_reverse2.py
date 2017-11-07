def isAlpabet(x):
    return x.isalpha()
def reverse(string):
    Lst = toList(string)
    r = len(Lst)-1
    l = 0
    while l < r:
        if not isAlpabet(Lst[l]):
            l += 1
        elif not isAlpabet(Lst[r]):
            r -=1
        else:
            Lst[1], Lst[r] = swap(Lst[l], Lst[r])
            l += 1
            r -= 1
        print("l and r are %d and %d" %(l,r))
    return toString(Lst)
def toList(string):
    l=[]
    for i in string:
        l.append(i)
    return l
def toString(l):
    return ''.join(l)
def swap(a, b):
    return b, a

string = "a!!b.c.d,e'f,ghi"
print("Input string "+string)
string = reverse(string)
print("Output string: ", string)
