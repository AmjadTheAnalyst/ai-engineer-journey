"""The Challenge: "Unique Email Redirection"
A large company is cleaning up its mailing list. 
Due to different typing habits, the same email address can look different in the system.
Your task is to count how many truly unique email addresses exist in a given list.
The Rules of Email Normalization:
Case Insensitivity: Emails are case-insensitive.Alice@Gmail.com is the same as alice@gmail.com.
The Plus Sign (+) Rule: Everything after a plus sign in the local name (before the @) is ignored. 
For example, bob+news@yahoo.com is actually delivered to bob@yahoo.com.
The Period (.) Rule: Periods in the local name are ignored. 
For example, c.a.t@gmail.com is the same as cat@gmail.com. 
(Note: Periods in the domain name after the @ must stay, like gmail.co.uk)."""

email_list = [
    "Alice@gmail.com",
    "alice.123@gmail.com",
    "bob+news@yahoo.com",
    "bob+work@yahoo.com",
    "b.o.b@yahoo.com",
    "ALICE@gmail.com"
]





#Concept
"""1. It Only Stores Unique Items If you try to .add() the exact same filename multiple times, a set will ignore the duplicates and only keep one copy.pythonnames = set()
names.add('report.csv')
names.add('report.csv')  # Python ignores this second line automatically

print(names)  # Output: {'report.csv'}"""