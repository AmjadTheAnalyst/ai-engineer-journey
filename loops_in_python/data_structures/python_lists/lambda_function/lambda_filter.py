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
