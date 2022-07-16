list1=eval(input("Enter list if numbers: "))


n=len(list1)
for j in range(n):
    for k in range(0,n-j-1):
        if list1[k] > list1[k+1]:
            list1[k],list1[k+1]=list1[k+1],list1[k]
print("sorted array:",list1)

result=[]
for i in list1:
    if i not in result:
        result.append(i)

print("duplicate removed: ",result)
        
