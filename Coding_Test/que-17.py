""" Write a function which takes input as a list of elements
and merge all strings seperated by '#' and add all numbers. Handle exceptions
"""
input_list = ["hello", 4 , "i" , 5, "know", "python", "2", 7]
total = 0
s1 = []
for item in input_list:
    try:
        if type(item)==str:
            s1.append(item)
        else:
            total = total + item
        
    except Exception as e:
        print(e)
l1 = "#".join(s1)
print(l1)
print("total", total)
