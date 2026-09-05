"""
#1 Python Challenge: Validate the Quality and Correctness of Email Values
Rules from the challenge:
1. Must not be empty
2. Must contain '.' and '@'
3. Must contain exactly one '@' symbol
4. Must end with '.com', '.org', or '.net'
5. Must not be longer than 254 characters
6. Must start and end with a letter or digit

Your Task:
Complete the 'validate_email' function below using Python conditionals 
(if/else statements, logical operators, and built-in string methods).
"""
email_address = input("Please enter your email address: ")
if len(email_address) == 0:
    print("invalid email address")
elif (len(email_address) > 254):
    print("invalid email address")
elif l
elif email_address.count("@") != 1:
    print("invalid email address")
elif email_address.endswith(".com") or email_address.endswith(".org") or email_address.endswith(".net"):
    print()
else:
    print("invalid email address")