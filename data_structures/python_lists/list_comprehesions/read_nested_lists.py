nested_words = [
    ["apple", "pear", "peach"],
    ["banana", "plum", "cherry"],
    ["grape", "pineapple", "mango"]
]
#task print pineapple
print(nested_words[2][1])
#grab the last word of each list
last_word = [
    word[-1]
    for word in nested_words
]
print(last_word)
#task: print only names who contain more than 6 characters
print([
    word 
    for sublist in nested_words for word in sublist 
    #we can use two for loops in same line in list comprehension
    if len(word) > 6
    ])

#what if i need all members starting from p
nested_words = [
    ["apple", "pear", "peach"],
    ["banana", "plum", "cherry"],
    ["grape", "pineapple", "mango"]
]
print([
    each_word
    for word in nested_words for each_word in word
    if each_word.startswith("p") == True    
])


#data_structures/python_lists/read_nested_lists.py