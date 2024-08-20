def greet():
    print('Hello', end=' ')
    print("Good morning")

def add(n1, n2):
    sum = n1+n2
    print(sum)

def multiple(n1, n2):
    mul = n1*n2
    return mul

def add_sub(n1, n2):
    sum = n1+n2
    differ = n1-n2
    return sum, differ

greet()

add(5,3)

res = multiple(2, 3)  # return 1 value
print(res)

res1, res2 = add_sub(5, 4)  # returns 2 values 
print(res1, res2)