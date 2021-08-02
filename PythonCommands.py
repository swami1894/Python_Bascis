# Print statement.
print("Hello, World!!\n")

# The zen of python.
import this

# Creating variables.
x = 255

# Display the datatype of the variable. Using string formatting.
print(f'\nDatatype of variable x is {type(x)}, containing data {x}')
print('')

# Creating another variable.
name = "Jane Doe"

# String datatype. Using string formatting.
print("Datatype of variable name is {}, containing data {}\n".format(type(name), name))

# Reading user input data.
a = input("Provide an number: ")
print(f"The input provided was {a} and the datatype of {type(a)}")
print(f"By default python reads data as string hence {type(a)}\n")

# Reading input as integer.
b = int(input("Provide a number: "))
print(f"The input provided was {b} and the datatype of {type(b)}\n")

# Reading input as float.
c = float(input("Provide a float value: "))
print(f"The input provided was {c} and the datatype of {type(c)}\n")
