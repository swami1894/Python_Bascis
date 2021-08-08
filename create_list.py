# Create a list
fruits = []

# Display an empty list
print("Created an empty list ", fruits)
print('')

# Add data fruits list.
fruits.append("Apple")
print("List after adding a member to the list ", fruits)

# Append user input.
fruits.append(input("Enter a fruit to add to the list: "))
print(f"After appending user data: {fruits}\n")

# List concatenation.
other_fruits = ["Oranges", "Pineapples", "Sweet Lime"]
fruits = fruits + other_fruits
print(f"List of other fruits {other_fruits}")
print(f"After concatenating fruits with other_fruits the list becomes {fruits}\n")

# Length of a list.
length_of_list = len(fruits)
print(f"Length of the fruits list {length_of_list}\n")

# List splicing and selecting the 2nd 3rd and 4th member in the list.
spliced_list = fruits[1:4]
print(f"Splicing the list to display 2nd 3rd and 4th member in the list {spliced_list}\n")

# Looping through the list.
for fruit in fruits:
    print(f"{fruits.index(fruit)}. {fruit}")
print("By default python index starts at 0.\n")

# delete a fruit from the list.
fruits.remove('Apple')
print(f"Deleteing Apple from the list {fruits}\n")

# Removing the list element from the list.
fruits.pop()
print("After removing the last element {}\n".format(fruits))

# Update Orange as Apple.
fruits[1] = "Apple"
print(f"Changing oranges to apples {fruits}")

#adding other_fruits to fruits.
fruits = fruits + other_fruits
print(f"Fruits that are available today {fruits}")

# Remove an element in the specific index. Removes the 4th element/ the 3rd index
fruits.pop(3)
print(f"After removing the 3rd index {fruits}")

# sort lsit in alphabetical or ascending order.
sorted_fruits = sorted(fruits)
print(f"Sorted does not modify the original list")
print(f"Variable sorted_list contains the sorted list {sorted_fruits}")
print(f"The original list is unmodified {fruits}")

#sort function modifies the original list hence must be used with care. Use sort
# only when you have no use for the original unsorted list.
copy_fruits = fruits
print(f"copy_fruits contains same list as fruits {copy_fruits}")
copy_fruits.sort()
print(f"After using sort function copy_fruits becomes {copy_fruits}")

# Arranging in descending order.
copy_fruits.reverse()
print(f"Sorting copy_fruits in descending order {copy_fruits}")

# This is an operation that shuffles the list to ensure the same type of shuffle
# happens each time from the library random use a fuction seed to with a whole
# number value.
from random import seed, shuffle
seed(250) # commnet this line to see the difference in the execution of shuffle
          # function
shuffle(copy_fruits)
print(f"After shuffeling {copy_fruits}")



# Deleting a variable.
del(copy_fruits)

# Try except block to continue the program from running so that the subsequent
# steps run
try:
    print(copy_fruits)
except Exception as e:
    print("Error:", e)
    pass     # Never use pass in a production programs since it is not a good
             # practic.
