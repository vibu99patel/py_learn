a=5
b=6
# using 3rd variable
temp = a
a=b
b = temp
print(a, b)

a=5
b=6
# without using 3rd variable 
a = a+b # 5+6 = 11
b = a-b # 11-6 = 5
a = a-b # 11-5 = 6
print(a, b)

a=5
b=6
# using xor
a = a^b
b = a^b
a = a^b
print(a, b)

a=5
b=6
#only in python (assignment swap)
a,b = b,a
print(a, b)