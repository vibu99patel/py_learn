num = 2.5
print(type(num))

num = 5
print(type(num))

num = 6+9j
print(type(num))

#casting
a = 5.6
b = int(a)
print(type(b))
print(b)

k = float(b)
print(k)

#complex numbers
k = 6
c = complex(b, k)
print(c)

#boolean
print(b>k)

print(int(True), int(False))

#list
lst = [25,36,45,12]
print(type(lst))

#set
s = {25,12,56,77}
print(type(s))

#tuple
t = (34,23,89,10)
print(type(t))

#string
str1 = 'navin'
print(type(str1))

#range
print(range(0,10))
print(list(range(0,10)))

#dictionary
d = {'navin':'samsung', 'rahul':'iphone', 'kiran':'oneplus'}
print(d.keys())
print(d.values())
print(d['rahul'])
print(d.get('kiran'))
print(type(d))
