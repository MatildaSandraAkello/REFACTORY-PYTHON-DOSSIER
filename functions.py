
# FUNCTIONS IN PYTHON
# A named blocked of code that performs a specific task is called 'FUNCTION'
# we use def name of function(): to define a function
# No Python Function should have the same name as a variable in the same python script
# Functions are not created they defined
# They are inactive after defining until invoked

numbers = [10, 20, 30, 40, 50, 60, 70, 80]    

def evens(): # this is a function called evens
    for number in numbers:
        if number % 2 == 0:
            print(number)

evens()            #this is us calling/ invoking a function 

fruits = ["apple", "banana", "mangoes", "berry"]           

def fruit(): # this is a function called fruit
    for items in fruits:
        print(items)   

fruit()      

def add():
    a, b = 20, 40
    print(a + b)

add()

#def add1():
    #a = int(input("Please enter your first number:\n ")) #\n helps us enter our data on the new line ie esc characters
    #b = int(input("Please enter your second number:\n "))
    #print(a + b)

#add1()    

def add2():
    a = int(input("Please enter your first number:\n ")) #\n helps us enter our data on the new line ie esc characters
    b = int(input("Please enter your second number:\n "))
    if a % b == 0:
        print(f"{a} doesn't have a remainder") # when using an f string to call our variable encase it in {}
    else:
        print(f"{a} gives a remainder")

add2()