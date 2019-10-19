n=int(input("Enter the limit"))

for i in range(1,n+1):
    for l in range(n-1):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print("\n")
    
for i in range(1,n):
    for m in range(n-1):
        print(" ",end="")
    for l in range(i):
        print(" ",end="")
    for j in range(n-i):
        print("*",end="")
    print("\n")