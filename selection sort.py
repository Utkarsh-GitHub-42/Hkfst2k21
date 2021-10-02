n=int(input("Enter the number of elements in the array : "))
a=[]
print("Enter the elements : ")
for i in range(0,n):
    e=int(input())
    a.append(e)
 
for i in range(0,len(a)):
    mini=i
    for j in range(i,len(a)):
        if a[j]<a[mini]:
            mini=j
    a[i],a[mini]=a[mini],a[i]   

print("The sorted array is : ",a)            
