n=input("\nEnter the limit")
for m in range(2*n-1):
    print(n,end="")
print("\n")
for i in range(n-1,0,-1):
    for m in range(n,i,1):
        print(m,end="")
    for l in range(2*i-1):
        print(l,end="")
    for m in range(n,i,1):
        print(m,end="")
    print("\n")
for m in range(2*n-1):
    print(n,end="")