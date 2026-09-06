names = ["ahmed", "yasin", "sheikh", " ", "Hassan"]
for name in names:
    if name == " ":
        continue
    print(name)
#...................
names = ["ahmed", "yasin", "sheikh", " ", "Hassan"]
for name in names:
    if name == " ":
        break
    print(name)
#................... 
#Pass statement, lets say i know there is a white space but i need to consult yet to what to do whith white space 
# so in that case i can mark Pass statement so that in later i can changes
# program will continue and keep rotating 
names = ["ahmed", "yasin", "sheikh", " ", "Hassan"]
for name in names:
    if name == " ":
        pass #todo
    print(name)