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
email = input("Please enter your email address: ")
#1. Must not be empty
if (len(email) == 0):
    print("Email adress must not be empty ")
#2. Must contain '.' and '@'
elif not('.' in email and '@' in email):
    print("Must contain '.' and '@'")
#3. Must contain exactly one '@' symbol
elif email.count("@") != 1:
    print("Must contain exactly one '@' symbol")
#4. Must end with '.com', '.org', or '.net'
elif not (email.endswith(".com") or email.endswith(".org") or email.endswith(".net")):
    print("Must end with '.com', '.org', or '.net'")
#5. Must not be longer than 254 characters
elif (len(email) > 254):
    print("Must not be longer than 254 characters")
#6. Must start and end with a letter or digit
elif not(email[0].isalnum() and email[-1].isalnum()):
    print("Must start and end with a letter or digit")
else:
    print("Valid email address:", email)
