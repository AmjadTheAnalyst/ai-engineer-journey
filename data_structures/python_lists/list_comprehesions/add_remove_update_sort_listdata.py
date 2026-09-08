#data_structures/python_lists/list_comprehesions/add_remove_update_listdata.py
#how to add add data in list
#at end use amethod .append
# A 3D List: [Truck][Shelf][Slot]
delivery_system = [
    # Truck 0
    [
        ["Apple", "Banana", "Cherry"],  # Shelf 0
        ["Donut", "Egg", "Fig"]         # Shelf 1
    ],
    # Truck 1
    [
        ["Grapes", "Honey", "Ice"],     # Shelf 0
        ["Juice", "Kiwi", "Lemon"]      # Shelf 1
    ]
]

#Task: Add the package "Mango" to the end of Truck 1, Shelf 0.
delivery_system[1][0].append("Mango")
print(delivery_system[1][0])
#what i want to add mango just after juice truck 1 and shelf 1
delivery_system[1][1].insert(1, "Mango")
print(delivery_system[1][1])

#Task 2: Add a brand new shelf containing ["Nuts", "Oatmeal"] to the end of Truck 0.
delivery_system.insert(1, ["Nuts", "Oatmeal"])
print(delivery_system[1])


############# Remove Methodologies ############
# a.clear() it will kill the whole list
# a.remove(value) it will first matched value menthioned
# a.pop(index number) it will remove the value at mentioned index number and return removed value
#in pop if index number is not mentioned, by default it removes the last index value
############# update Methodologies ############
# a[index number] = new value

############# sortation Methodologies ############
a = [1,7,8,0,3,7,5,4,6,7]
print(a.sort())
#it will return none because sort() itself does not sorted list, its only modifies original list
#Run the sorting mechanism on its own line, and then print the list a.
a = [1, 7, 8, 0, 3, 7, 5, 4, 6, 7]
a.sort()  # This modifies 'a' behind the scenes

print(a)

#If you want to sort and print on a single line, 
# use Python's built-in sorted() function. Unlike .sort(), 
# sorted() creates and returns a brand-new sorted copy of the list.
a = [1, 7, 8, 0, 3, 7, 5, 4, 6, 7]

# sorted() returns the new list directly to the print function
print(sorted(a))
# Output: [0, 1, 3, 4, 5, 6, 7, 7, 7, 8]                 

#how to sort inverse
print(sorted(a, reverse = True))



########## copy list ############
a = [1,2,3,4,5,6]
a.copy() #best for non-nested lists (shallow copy)
a.deepcopy() #best for nested list in order to copy inner lists aswell



############# how to combine lists ########
# +, *
# l1+l2 concatinate both lists
# l1*2 
