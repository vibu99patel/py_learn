def add(a,b):   # a, b are formal arguments 
    c = a+b
    print(c)

add(5, 6)
print()

# actual arguments have 4 types: position, keyword, default, variable length
#postition
def person(name, age):  
    print(name)
    print(age)

person(28, 'navin')
print()

#keyword
def person(name, age):  
    print(name)
    print(age)

person(age=28, name='navin')
print()

#default
def person(name, age=28):  
    print(name)
    print(age)

person("navin")
print()

#variable length (forms a tuple)
def sum(*b):  
    c = 0
    for i in b:
        c += i
    print(c)

sum(5,6, 34, 78)