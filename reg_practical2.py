import re
Nameage = '''
Janice is 22 and Theon is 33
Sagar is 25 and Joey is 32
'''
ages = re.findall(r'\d{1,3}', Nameage)
names = re.findall(r'[A-Z][a-z]*', Nameage)

ageDict = {}
x = 0
for eachname in names:
    ageDict[eachname] = ages[x]
    x +=1
print(ageDict)

print("*#"*9)

Str = "Sat, hat, pat,mat"

allStr = re.findall("[Shmp]at", Str)

for i in allStr:
    print(i)

print("*#"*9)
num ="123, 1234, 12345, 123456, 1234567"
print("Matches: ", len(re.findall("\d{5,7}", num)))
 
