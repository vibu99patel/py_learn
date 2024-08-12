# array contains same data type 
from array import array
# same as above: import array as arr
vals = array('i',[5,9,8,4,2])
print(vals)

print(vals.buffer_info())  #to get size and address
vals.reverse()
print(vals)

for i in vals:
    print(i) 
#or 
for i in range(len(vals)):
    print(vals[i])

# 'u' - character 
# 'i' - integer

# to copy the array into new one 
new_arr = array(vals.typecode, (a for a in vals))
for e in new_arr:
    print(e)

# dynamically create array
arr = array('i', [])

n = int(input("Enter the length of array:"))
for i in range(n):
    x = int(input("Enter value: "))
    arr.append(x)

print(arr)

# search the value in array
val = int(input("Enter value to search: "))
k=0
for i in arr:
    if val == i:
        print(k)
        break
    k+=1

