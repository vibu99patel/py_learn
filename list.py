# list are mutable so they can be changed 

nums = [25,12,36,95,14]

print(nums)
print(nums[0])
print(nums[4])
print(nums[2:])
print(nums[-1])

names = ['navin', 'kiran', 'john']

val = [9.5, 'navin', 25]

mil = [nums, names]
print(mil)

nums.append(45)  # adds at end 
print(nums)

nums.insert(2,77)   # adds at certain index, insert(indx, val)
print(nums)

nums.remove(14) # removes value
print(nums)

nums.pop(1)  # removing at specific index
print(nums)

del nums[2:]  # deleting 
print(nums)

nums.extend([29,12,16,36]) # adding multiple values 
print(nums)

print(min(nums), max(nums))

nums.sort()
print(nums)

print(nums[1:5:3])