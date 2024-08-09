x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = x+y
print(z)

# to get 1 char
ch = input("Enter a character: ")
print(ch[0])
#or you could
ch = input("Enter a character: ")[0]
print(ch)

res = eval(input("Enter an expression: "))
print(res)

#taking arguments in cmnd 
import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
z = x+y
print(z)