#Input is a mechanism that allows a user input variables from a keyboard.
#Input outputs are by default intergers even numbers so you must convert them back to 'int' ie int(input())
#num1 = input("input your number here") #Using a function we can prompt user to input values in the memory space from a keyboard
#print("your number is:", num1)

"""
This is called multi-line commenting.
This is another way of commenting in Python. 
Allows you write comments on multiple lines for readability
"""

#name = input("input your name here")
#print("Hello ", name)       

# The 'input' function will consider everything entered/captured from the keyboard as a string value
#print(type(name))

#changing variables from one type to another is called 'TYPE CASTING' e.g int to string

age = int(input("Input your age here"))


if age < 18:
    print("Minor")
elif age < 21:
    print("young adult")
else:
    print("adult")