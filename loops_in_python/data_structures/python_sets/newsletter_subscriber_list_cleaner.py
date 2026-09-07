"""📧 The Challenge: Clean the Newsletter Subscriber ListYou are building a 
sign-up form for a company newsletter. People typed in their email addresses, 
but the database is messy. Some people signed up multiple times, 
some had accidental Caps Lock on, and some added extra spaces at 
the ends of their emails.Your goal is to process the raw email list 
using a for loop to get a clean set of unique, valid subscriber emails."""

raw_emails = [
    " alice@email.com", 
    "bob@email.com", 
    "ALICE@EMAIL.COM", 
    "charlie@email.com ", 
    "bob@email.com", 
    "Alice@email.com"
]
cleaned_list = set()
for email in raw_emails:
    list = email.strip().lower()
    cleaned_list.add(list)
print(cleaned_list)
