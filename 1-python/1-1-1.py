name = input("Enter your name: ") 
print ("Hello, World!")
print("Hello, " + name + "!")

# how to debug, 
# open debugger, select python debugger, and select a breakpoint for the file


# interpolation
print(f"Hello, {name}!")
print (f"{50} + {50} = {50+50}")

# duck typing - gets it data value from the variable assignment
age = 30 # int
gpa = 3.4 # float

# type cohersion - assigning the type of variable to the data value
age = int("99") 
gpa = float("3.4")
# both of these start (assigned) as strings and then are cohersed into being a different data type
age = input("Enter your age:") # the type is str
pass

print("57"/3) 

