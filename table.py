n=int(input("Enter the number :"))
mul=1
print( n,"!=",end=" ")
for i in range(1,n+1,1):
    mul*=i
    print(i,end=" ")
    if i < n:
        print("*",end=" ")
print(f"={mul}")
