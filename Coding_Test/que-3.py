"""Write the code to Initialize a dictionary in python
and save json of the dictonary in a file?"""

exDict = {}
exDict['Sagar']={
    'name':'Sagar',
    'address':'Mumbai, MH',
    'phone':9094785475
    }
exDict['Vinay']={
    'name':'Vinay',
    'address':'Pimpri,Pune, MH',
    'phone':9092346534
    }

import json
s= json.dumps(exDict)
print(s)
with open("dictionary.txt","w") as f:
    f.write(s)
