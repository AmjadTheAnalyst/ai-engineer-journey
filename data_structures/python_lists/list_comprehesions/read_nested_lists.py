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

