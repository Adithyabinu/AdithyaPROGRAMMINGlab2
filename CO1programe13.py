n=int(input("enter a limit:"))
print("enter",n,"colour names:")
c=[]
for i in range(0,n):
    c.append(input())
print("the first and last colours are:")
for i in range(0,n):
    print(c[0],c[n-1])
    break