Hundred,Fifty,Ten=0,0,0
n=int(input("Enter the amount to be withdrawn : "))
while n>0:
    if n%10!=0:
        print("Invalid Input")
    if n>=100:
        Hundred=n//100
        n=n%100
    if n>=50:
        Fifty=n//50
        n=n%50
    if n>=10:
        Ten=n//10
        n=n%10
print(Hundred,Fifty,Ten)
  
        
        
