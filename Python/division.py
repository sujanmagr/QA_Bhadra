#to calculate user marks division

marks=int(input("Enter your marks: "))
if marks>=80:
    if marks>100:
        print("Invalid marks")
    else:
        print("You got distinction")
elif marks>=60:
    print("You got first division")
elif marks>=40:
    print("You got second division")
else:
    print("You are failed")

