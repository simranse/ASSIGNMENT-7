def binarySearch(list1,key):
    low=0
    high=len(list1)-1
    found=False
    while low<=high and not found:
        mid=(low+high)//2
        if key==list1[mid]:
            found=True
        elif key>list1[mid]:
            low=mid+1
        else:
            high=mid-1
    if found == True:
        print("element is found")
    else:
        
        print("element is found")
list1=eval(input("Emter elements of list: "))
list1.sort()
print("sorted array:",list1)
key=int(input("Enter the key: "))
count=list1.count(key)
print("occurance of key is:",count)
binarySearch(list1,key)
    
