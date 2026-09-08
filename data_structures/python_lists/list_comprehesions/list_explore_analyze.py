items = ['apple', 'banana', 'cherry']
print(len(items))  # Output: 3

numbers = [42, 7, 19, 88, 3]
print(max(numbers))  # Output: 88
print(min(numbers))  # Output: 3

"""3. all(list) — Check if EVERYTHING is TrueReturns True only if every single 
element in the list evaluates to True (or if the list is empty). 
If even one item is "Falsy" (like 0, False, None, or an empty string ""), 
it returns False."""

# All elements are non-zero integers (Truthy)
print(all([1, 2, 3]))    # Output: True

# Contains a 0 (Falsy)
print(all([1, 0, 3]))    # Output: False

# Contains one Truthy value (the number 5)
print(any([0, False, 5]))  # Output: True

# Everything is Falsy
print(any([0, False, ""])) # Output: False

#real usecase of all/any with list comprehensions
scores = [85, 92, 78, 90, 88]
criteria = [
    score
    for score in scores
    if score > 70
]
print(criteria)
#this will only return the numeric values  greater, 
# but what if i need true false answer
scores = [85, 92, 78, 90, 88]
criteria = [
    score
    for score in scores
    if score > 70
]
print(criteria)