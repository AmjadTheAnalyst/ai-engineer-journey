#Problem 1
numbers = [1, 2, 3, 4, 5]
# generate a new list displaying the square of each number
squared_numbers = [
    n*n
    for n in numbers
]
print(squared_numbers)

#new task added, take square for only even numbers
numbers = [1, 2, 3, 4, 5]
# generate a new list displaying the square of each number
squared_numbers = [
    n*n
    for n in numbers
    if n % 2 == 0
]
print(squared_numbers)