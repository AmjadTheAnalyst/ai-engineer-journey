prices = [120, 30, 300, 80]
#return all prices greater than 100
#filter
#price > 100 True (this is a custom logic, not a python function, so we will handle it with lambda)
print(list(filter(lambda p: p>=100, prices)))

#Problem2
numbers = [-5, 3, 0, 12, -8, 7, -1, 4]
#return only positive numbers
#simple logic n > 0
#lambda n : n > 0  (custom logic)
print(list(filter(lambda n : n > 0, numbers)))

#Problem 3
words = ["apple", "cat", "banana", "dog", "kiwi", "python", "it"]
#return values having characters less than 5
#lambda word : len(word) < 5 (customized logic)
print(list(filter(lambda word : len(word) < 5, words)))

#Problem 4
numbers = [14, 21, 35, 42, 57, 68, 73, 80]
#return only even numbers
# lambda n : n%2 == 0
print(list(filter (lambda n : n%2 == 0, numbers)))

#problem 5
scores = [12, 25, 34, 50, 55, 61, 70, 84, 95]
#extract only the numbers that are multiples of 5
#logic n % 5 == 0
lambda n: n% 5 == 0
print(list(filter (lambda n: n% 5 == 0, scores)))

#problem 6
characters = ['a', 'B', 'c', 'D', 'e', 'F', 'g', 'H']
#return only uppercase letters
print(list(filter(str.isupper, characters)))

#problem 7
ages = [5, 12, 13, 16, 19, 20, 25, 14]
#return only TEEN AGES
#custom logic age >= 13 or age <=19
print(list(filter(lambda age:age >= 13 and age <=19, ages )))


# Your starting list
ages = [14, 21, 17, 18, 32, 16, 45, 12, 19]
"""The Challenge: Filter the AdultsYou are given a list of ages. 
Write a Python program to extract only the ages that are 18 or older."""
print(list(filter (lambda age : age >= 18, ages)))

