av = 5
x = int(input("How many candies you want? : "))
i = 1
while i <= x:
    if i > av:
        print("out of stock")
        break  #to get out of loop
    print("candy")
    i+=1

print("bye")

for i in range(1, 101):
    if (i%3==0) or (i%5==0):
        continue  #to skip it thru
    print(i, end=" ")

print("bye")

for i in range(1, 101):
    if (i%2 == 0):
        pass   # if we dont know wht the condition is  
    else:
        print(i, end=" ")