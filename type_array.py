from numpy import *
#array
arr = array([1,2,3,4,5])
print(arr.dtype)
print(arr)

#linspace
arr = linspace(0,15) #create parts
print(arr)

#arange
arr = arange(1,15,2) #steps 
print(arr)

#logspace
arr = logspace(1, 40, 5) #creates based on num's log()
print(arr)

#ones
arr = ones(5, int) #gives u 1's in int format 5 times
print(arr)