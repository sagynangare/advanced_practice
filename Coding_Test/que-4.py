#Write a code to Read a file and append lines to a list?
i=raw_input("Enter text you want to enter in a file: ")
with open("read_append.txt","a") as f:
    f.write('\n')
    f.write(i)
    
    
