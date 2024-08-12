# divisible by 1 or by itself like 7, 13, 19

num = int(input("Enter a number to check if it's prime or not: "))

for i in range(2, num):
    if num % i == 0:
        print("not prime")
        break
else: 
    print("prime")
   