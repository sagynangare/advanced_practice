def product10(a):
    return a*10
list1 = range(10)
m = map(product10,list1)
print("Function(m): ",m)

for i in m:
    print("M(m): ",i)
m2=map((lambda a:a*10),list1)
for i in m2:
    print("M(m2): ",i)
    
