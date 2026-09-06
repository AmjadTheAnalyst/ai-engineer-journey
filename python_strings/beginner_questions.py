
# CHALLENGE 1: Remove All Vowels
# ---------------------------------------------------------------------
# Goal: Take a string and return a new version with all vowels removed.
# Example: "coding journey" -> "cdng jrny"
# Hint: Vowels are 'a', 'e', 'i', 'o', 'u' (check both lower and upper case).

text = "enter"
result = ""
for ch in text:
    if ch in {'a', 'e', 'i', 'o', 'u'}:
        continue
    result = result + ch
print(result) #expected output: ntr