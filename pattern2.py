

n=int(input("\n Enter the first input"))
x=int(input("\n Enter the second input"))
    
for i in range(1,n+1):
    for l in range(n-1):
            print(" ",end="")
    for s in range(x):
        
        for j in range(i):
            print("*",end="")
        for a in range(n1):
            print(" ",end="")
        
    n1=n1-1
    print("\n")
    
n1=2
for i in range(1,n):
    
    for m in range(n-1):
            print(" ",end="")
    for l in range(i):
            print(" ",end="")
    for s in range(x):
       
        for j in range(n-i):
            print("*",end="")
        for a in range(n1):
            print(" ",end="")
        
    n1=n1+1
    print("\n")
   



