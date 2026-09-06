"""
Python Challenge: Validate the Quality and Correctness of Passwords

Rules from the challenge:
1. Must not be empty
2. Must be at least 8 characters
3. Must include at least 1 uppercase letter
4. Must include at least 1 lowercase letter
5. Must not be the same as the email
6. Must not contain any spaces
7. Must start and end with a letter or digit

Your Task:
Complete the 'validate_password' function below using Python conditionals,
loops, and built-in string methods.
"""
password = "@ength123"
email = "email"
#1. Must not be empty
if len (password) == 0:
    print("Must not be empty")
#2. Must be at least 8 characters
if len(password) < 8:
    print("Must be at least 8 characters")
#3. Must include at least 1 uppercase letter
#4. Must include at least 1 lowercase letter
has_upper = False
has_lower = False
for char in password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
if not has_upper or not has_lower:
    print("Must include at least 1 uppercase letter")
#5. Must not be the same as the email
if password == email:
    print("Must not be the same as the email")
#6. Must not contain any spaces
password1 = password.replace(" ","")
if len(password1) != len(password):
    print("Must not contain any spaces")
#7. Must start and end with a letter or digit
if not password[0].isalnum() or not password[-1].isalnum():
    print("Must start and end with a letter or digit")