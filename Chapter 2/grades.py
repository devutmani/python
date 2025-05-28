courseName = input("Enter course name: ")
marks = float(input(f"Enter marks of {courseName}: "))

if (marks >= 90 and marks <= 100):
    print(f"You got A in {courseName}")

elif(marks >= 80 and marks < 90):
    print(f"You got B in {courseName}")

elif(marks >= 70 and marks < 80):
    print(f"You got C in {courseName}")

elif(marks >= 33 and marks < 70):
    print(f"You got D in {courseName}")

else:
    print("Failed, but don't worry, you know bilgates got failed in his 10th exam")
    
print("Thanks for using our application")