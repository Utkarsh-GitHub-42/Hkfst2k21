import time
def insertion_Sort(arr):
 for i in range(1, len(arr)):
     grt = arr[i]
     j = i-1
     while j >= 0 and grt < arr[j] :
         arr[j + 1] = arr[j]
         j -= 1
     arr[j + 1] = grt

 return arr

n=int(input("Enter the number of elements in the array : "))
a=[]
print("Enter the elements : ")
for i in range(0,n):
    e=int(input())
    a.append(e)
t=time.time()    
print(insertion_Sort(a))
print(time.time()-t)
