for i in range(4):     #square
    for j in range(4):
        print("# ", end=" ")
    print()
print()
for i in range(4):     #triangle
    for j in range(i+1):
        print("# ", end=" ")
    print()
print()
for i in range(4):     #reverse triangle 
    for j in range(4-i):
        print("# ", end=" ")
    print()

