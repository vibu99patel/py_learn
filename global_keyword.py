#scope
a=10      #global

def something():
    a=15      #local
    print('in func:', a)

something()

print('outside:', a)
print()

#to change global variable in function 
def something():
    global a
    a=15      #local
    print('in func:', a)

something()

print('outside:', a)
print()

#globals and locals in function 
a=10
print(id(a))

def something():
    a=9
    x=globals()['a']
    print(id(x))
    print('in func:', a)

    globals()['a']=15


something()

print('outside:', a)
