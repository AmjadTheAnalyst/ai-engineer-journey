#Write a program that take a number from user and check whether its even or odd
number = int(input("Please enter any number: "))
if number % 2 == 0:
    print("You entered an even number")
else:
    print("You entered an odd number")
#what if user enter a negative number -- not acceptable
number = int(input("Please enter any number: "))
if str(number).startswith("-"):
    print("Negative numbers are not allowed")
elif number % 2 == 0:
    print("You entered an even number")
else:
    print("You entered an odd number")
#what if user enter a pointing number -- not acceptable
number = int(input("Please enter any number: "))
for ch in str(number):
    if ch == ".":
        print("Point numbers are not allowed")
    elif str(number).startswith("-"):
        print("Negative numbers are not allowed")
    elif number % 2 == 0:
        print("You entered an even number")
    else:
        print("You entered an odd number")

#4.5

