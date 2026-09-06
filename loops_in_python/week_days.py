#write a program to print weekdays and but skip weekends.
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for weekday in weekdays:
    if weekday in {"Saturday", "Sunday"}:
        break
    print(weekday)
