t1=int(input("Enter a marks1: "))
t2=int(input("Enter a mark2: "))
t3=int(input("Enter a marks3: "))
if(t1<=t2 and t1<=t3):
       average=t2+t3/2
elif(t2<=t1 and t2<=t3):
    average=t1+t3/2
else:
    average=t1+t2/2
print("The average marks=",average)
