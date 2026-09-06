#All about sets 06.sep.2026

"""
sets are un-ordered
sets are mutable (its mean we can delete etc any item once its already created)
sets are non-indexed (we can not access any element of set by its index)
ofcourse sets contain only unique values , duplicates are not allowed
"""
#set methods
#how to add values in sets:
a = {5,10,15,20}
a.add(50)
print(a)
#value remove
a.remove(5) #if value is not in set, it will crash the code
a.discard(5) #it will not crash the code if value is not in set.
#what if we want to add multiple values in set once
#we can pass it a iterable(string, set, list etc)
a.update("hiii") #it will add only h and i coz i is three times
print(a)

#Mathematical methods
b = {1,2,3,4}
c = {2,4,6,8,0}
#union
print(b.union(c)) #only unique values
#intersection
print(b.intersection(c)) #only common values in both sets
#opposite of intersection (only non common values)
print(a.symmetric_difference(b)) #nomatters from where starts a or b
#difference
print(a.difference(b)) #items in a but not in b
print(b.difference(a)) #items in b but not in a

#Relationships Methods
#subset
print(a.isubset(b))
#if a is a subset of b if yes True if no False














