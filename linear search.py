a=[]
flag=0
n = int(input("Enter number of elements : "))
for i in range(0, n):
    element = int(input())
    a.append(element)
e=int(input("Enter the element to be searched : "))    
for i in range(0,len(a)):
    if a[i]==e:
        print("Element found at position :",i)
        flag=1
if flag==0:
    print("Element not found")



    
# Binary Search
def binary_search(arr, x):
    arr.sort()
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
       
        if arr[mid] < x:
            low = mid + 1
        
        elif arr[mid] > x:
            high = mid - 1
       
        elif arr[mid]==x:
            return "Element found"
 
    return "Not found"
a=[]
n = int(input("Enter number of elements : "))
for i in range(0, n):
    element = int(input())
    a.append(element)
ele=input()
print(binary_search(a, ele))

