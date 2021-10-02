import random
import time
n=int(input("Enter the number of elements in the array : "))
a=[]
for i in range(0,n):
    a.append(random.randint(1,1000))
print("The array taken is: ",a)
c=time.time()
for i in range(len(a)):
             mini=i
             for j in range(i,len(a)):
                 if a[j]<a[mini]:
                     mini=j
            
             a[i],a[mini]=a[mini],a[i]
    
print("Time taken : ",time.time()-c)
print("The sorted array is : ",a)

