def bin2Dec(val):
    return int(val, 2)

def Oct2Hex(val):
    deval=int(val,8)
    return hex(deval)

try:
    num1 = input("Enter a binary number: ")

    print(bin2Dec(num1))

except ValueError:
    print("Invalid literal in input with base 2")

try:
    num2 = input("Enter an octal number: ")
    print(Oct2Hex(num2))

except ValueError:
    print("Invalid literal in input with base 8")
