# Bubble Sort
lst =[1,2,3,5,7,9,5,9,8,0]

for j in range(0,10):
    check_for_swap = False
    for i in range(0,9):
        if lst[i] >lst[i +1]:
            swap = lst[i]
            lst[i] = lst[i+1]
            lst[i+1]=swap
            check_for_swap = True
        if check_for_swap == False:
            break
print(j,lst)
