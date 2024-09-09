
def fib(n):

    if n < 1:    # for negative numbers 
        print('invalid input')
        return 0
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            if c < 100:   #we want to print less than 100 
                a = b
                b = c
                print(c)

fib(100)