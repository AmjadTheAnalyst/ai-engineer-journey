#scan emails to block unsafe data to entering your system.
emails = [
    "data@gmail.com",
    "amjad@outlook.de",
    "drop table users;"  ,   #sql_injection
    "maria@gmail.com"
]
for email in emails:
    if ";" in email:
        print("This is a hacker attack, sql injection")
        break
    print(f"Processing Email: {email}")