#05.09.2026
#Basic casting: Store the string "42" in a variable. Cast it to an integer, add 8 to it, and print the result.
variable = "42"
print(type(variable))
variable = int("42")
print(type(variable))
add = variable + 8
print(add)

#Floor division & modulo: You have 17 candies to split evenly among 5 friends. 
# Write code that prints how many candies each friend gets, and how many candies are left over. (Use // and %.)
candies = 17
friends = 5
distribution = 17 // 5
left_over = 17 % 5
print("how many candies each friend gets:", distribution)
print("how many candies are left over:", left_over)

#Type error, on purpose: Store age = "30" (as a string) and bonus = 5 (as an int). 
# Try to print age + bonus without casting anything. Run it, read the actual error message Python gives you, 
# and write one sentence explaining what it means in your own words.

age = "30"
bonus = 5
total = age + bonus
print(total)

#TypeError: can only concatenate str (not "int") to str
#so python throw a typeerror because it not automatically cast the type so its unable to concatenate string into integers.

#Fix it: Now fix problem 3 so it correctly prints 35 by casting appropriately.
age = "30"
bonus = 5
total = int(age) + bonus
print(total)

#Comparison operators: Store two numbers of your choice. Print the results of checking: are they equal? Is the first greater than the second?
#  Is the first less than or equal to the second? (Three separate print statements, three comparison operators.)

a = 23
b = 35
if a==b:
    print(f"Numbers {a}, {b} are equal")
if a>b:
    print(f"Number {a} is greater than {b}")
if a<b:
    print (f"Number {a} is less than {b}")


#Mini challenge — combine everything: A user enters their height in centimeters as a string: height_str = "175". 
# Convert it to an integer, then print whether the person is "tall" (over 170cm) or "average" using 
# a comparison operator and an f-string in your print statement.
height = input("Enter your height in cm: ")
#print(type (height))
height = int(height)
#print(type (height))
if height > 170:
    print("The person is tall")
if height < 170:
    print("The person is average")
