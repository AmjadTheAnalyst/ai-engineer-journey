# ============================================================
# PYTHON PRACTICE — SECRET CODE ANALYZER
# ============================================================
# You are given a secret code:
code = "PyThOn2026DataScience"
# 1. How many uppercase letters are in the code?
# 2. How many lowercase letters are in the code?
# 3. How many numbers are in the code?
upper_str = ""
lower_str = "" 
num_str = ""
for ch in code:
    if ch.isupper():
        upper_str = upper_str + ch
    elif ch.islower():
        lower_str = lower_str + ch
    elif ch.isdigit():
        num_str = num_str + ch 
print (f"Total Upper Case Letters {len(upper_str)}")
print(f"Total lower Case Letters {len(lower_str)}")
print(f"Total digits are {len(num_str)}")

if len(upper_str) >= 3 and len(lower_str) >=5 and len(num_str) >=4:
    print("Password is very strong")
elif len(upper_str) >= 2 and len(lower_str) >=5 and len(num_str) >=2:
    print("Password is strong")
else:
    print("Password is weak")