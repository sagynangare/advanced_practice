import numpy as np
from operator import itemgetter
from heapq import nlargest

rand_horse=np.random.random_integers(101,size=(5,5))
faster_horse=np.amax(rand_horse)
iterations = 0

second = np.max(np.partition(rand_horse, 2)[2])
print("Second faster ", second)

third = np.max(np.partition(rand_horse, 3)[3])
print("Third fater ", third)


##for i in np.nditer(rand_horse):
##    if np.amax(i, axis = 0):
##        print("Fastest horse is at: " + str(next((i,j) for i,x_i in enumerate(rand_horse) for j, x_ij in enumerate(x_i) if x_ij==np.amax(rand_horse))))
##        iterations +=1
##        break
##    elif np.amax(i, axis =1):
##        pass
for i,x_i in enumerate(rand_horse):
    for j, x_ij in enumerate(x_i):
        if x_ij==np.amax(rand_horse):
            print("Trial ",(i,j))
            
       

print("Random Horses = "+ str(rand_horse))
x=next((i,j) for i,x_i in enumerate(rand_horse) for j, x_ij in enumerate(x_i) if x_ij==np.amax(rand_horse))
print("Fastest Horse is "+str(faster_horse)+ " at position "+str(x))


second = np.max(np.partition(rand_horse, 2)[2])
#x1=next((i,j) for i,x_i in enumerate(rand_horse) for j, x_ij in enumerate(x_i) if x_ij== second)
print("Second faster " + str(second) + " at position "+str(x1))

third = np.max(np.partition(rand_horse, 3)[3])
print("Third fater ", third)




##it= np.nditer(rand_horse)
##while not it.finished:
##    if it == faster_horse:
##        print("Faster horse is at %d <%d>" %(it[0], it.index))
##        it.iternext()
"""for i in np.nditer(rand_horse.T):
    if i == faster_horse:
        print("This is fastest horse: " + str(i))

"""







##def largest_indices(ary,n):
##    flat = ary.flatten()
##    indices = np.argpartition(flat, -n)[-n:]
##    indices = indices[np.argsort(-flat[indices])]
##    return np.unravel_index(indices, ary.shape)
##
##print("Fastest Horse is ",largest_indices(rand_horse, 3))

