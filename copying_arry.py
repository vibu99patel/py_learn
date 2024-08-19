from numpy import *

#vectorized ops
arr1 = array([1,2,3,4,5])    
arr2 = array([6,1,9,3,2])    
arr3 = arr1 + arr2
print(arr3)

#math ops
arr = array([1,2,3,4,5])    
print(sin(arr))
print(cos(arr))
print(log(arr))
print(min(arr))
print(max(arr))

#copying/aliasing
arr4 = array([2,6,8,1,3])
arr2 = arr4
print(arr4)
print(arr2)

print(id(arr2))
print(id(arr4))

#create 2 differ array
arr4 = array([2,6,8,1,3])
arr2 = arr4.view()  #same content with different address 

arr4[1] = 7  #shallow copy - changes in both arrays

print(arr4)
print(arr2)

print(id(arr2))
print(id(arr4))

#create 2 differ array
arr4 = array([2,6,8,1,3])
arr2 = arr4.copy()  #same content with different address 

arr4[1] = 7  #deep copy - changes in only one array

print(arr4)
print(arr2)

print(id(arr4))
print(id(arr2))