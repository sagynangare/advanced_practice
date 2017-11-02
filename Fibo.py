#n =int(raw_input("Please enter how much fib sequence you want! "))

def fib(n):
    if n<2:
        return(n)
    return fib(n-2)+fib(n-1)
print(fib(12))
