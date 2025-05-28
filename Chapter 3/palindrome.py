list = []

list.append(input("Enter element 1: "))
list.append(input("Enter element 2: "))
list.append(input("Enter element 3: "))
list.append(input("Enter element 4: "))

print(list)

palindrome = False
i = 0
while (i < len(list)):
    if (list[i] == list[len(list)-1-i] and i == len(list) - 1):
        palindrome = True
        break
    i += 1

if (palindrome == True):
    print("Yes, it's a palindrome!")
else:
    print("Not a palindrome!")