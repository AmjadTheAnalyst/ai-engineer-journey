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

                    