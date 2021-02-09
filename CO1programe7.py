list=[1,2,3,4,5]
list1=[5,7,8,9,78]
c=int(0)
a=int(0)
for i in list and list1:
    if len(list)==len(list1):
        print("list are of same length")
        break
    else:
        print("list have different length")
        break
for i in range(0,len(list) and len(list1)):
        c=c+list[i]
        a=a+list1[i]
for i in range(0,len(list)and len(list1)):
        if a==c:
            print("sum of values are same")
            break
        else:
                print("sum of values are different")
                break
print("elements that matched are:")
l=[]
for i in range(0,len(list)):
    for j in range(0,len(list1)):
            if list[i]==list1[j]:
                    l.append(list[i] and list1[j])
            else:
                p=i
                continue
print(l)
                    