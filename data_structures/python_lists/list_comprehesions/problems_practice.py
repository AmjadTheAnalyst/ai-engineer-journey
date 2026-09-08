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

#Problem 2
names = ["alice", "bob", "charlie"]
#convert them all into upper case
upper_names = [
    name.upper()
    for name in names
    #so we dnt need to filter the data, as we convert all
]
print (upper_names)