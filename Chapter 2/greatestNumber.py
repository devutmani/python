num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))

if (num1 > num2):
    if (num1 > num3):
        print(num1, "is the greatest number amoung", num1, ",", num2, "and", num3)
    else:
        print(num3, "is a greatest number amoung", num1, ",", num2, "and", num3)
else:
    if(num2 > num3):
        print(num2, "is a greatest number amoung", num1, "", num2, "and", num3)
    else:
        print(num3, "is a greatest number amoung", num1, ",", num2, "and", num3)