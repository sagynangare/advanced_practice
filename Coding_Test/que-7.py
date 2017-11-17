#code to catch an Exception in python?
x= int(raw_input("Enter a number1: "))
y= int(raw_input("Enter a number1: "))

try:
    z= x/y
except Exception as e:
    print("Error occures:", e)
    z= None
print("Division is: ",z)
