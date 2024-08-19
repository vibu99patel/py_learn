from numpy import *

arr1 = array ([
                    [1,2,3,6,2,9],
                    [4,5,6,7,5,3]
                    
            ])

print(arr1.dtype) # gives type 
print(arr1.ndim)  #gives dimensions
print(arr1.shape) #gives rows and columns
print(arr1.size)

# creates 1 dimensional
arr2 = arr1.flatten()
print(arr2)

# creates 2/3 dimensional
arr3 = arr2.reshape(3,4)
print(arr3)
arr4 = arr2.reshape(2,2,3)
print(arr4)

arr5 = array ([
                    [1,2,3,6],
                    [4,5,6,7]
                    
            ])

#matrix
m = matrix(arr5)
print(arr5)

m = matrix('1 2 3 ; 4 5 6 ; 1 6 7')
print(m)

print(diagonal(m))
print(m.min())

m1 = matrix('1 2 3 ; 6 4 5 ; 1 6 7')
m2 = matrix('1 2 3 ; 4 8 5 ; 2 6 7')

m3 = m1 + m2
print(m3)

m4 = m1 * m2
print(m4)
