#lets practice some functions and methods on lists
l = [[1,2,3],[4,5,6],[7,8,9]]
#i want to add a new list memebr at the end
l.append([7,9,8])
print(l)
#now i want to add the same list member but on very start
l = [[1,2,3],[4,5,6],[7,8,9]]
l.insert(1, [7,9,8])
print(l)

a = [[1,2], [3,4]]
removed = a.pop([0,1])
print(removed)