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
