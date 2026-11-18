#Conditional Statement
'''
if condition:
    # do something
elif condition:
    do something

elif condition:
    do something
else:
    # do something else
'''

# if 10>3:
#     print(10-3)
#     print("Ten is greater than three!")
# else:
#     print(10+3)

number1=int(input("Enter Number1: "))
number2=int(input("Enter Number2: "))

if number1>number2:
    print("Number1 is greater than Number2")
elif number1==number2: 
    print("Number1 is equal to Number2")
else:
    print("Number2 is greater than Number1")