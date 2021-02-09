a=[]
k=int(input("enter a limit:"))
print(f"enter {k} values")
for i in range(0,k):
    a.append(int(input()))
    print("\n the list after assigning:\n")
    for i in range(0,len(a)):
        if a[i]>=100:
            print("over")
        else:
                print(a[i])