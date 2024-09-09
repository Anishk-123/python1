Val=int(input("Enter a value"))
str_val=str(Val)
if (str_val==str_val[:: -1]):
    print("Palindrom a:")
else:
    print("Not Palindrome")

for i in range(10):
    if str_val.count(str(i))>0:
        print(str(i),"appears",str_val.count(str(i)),"times")