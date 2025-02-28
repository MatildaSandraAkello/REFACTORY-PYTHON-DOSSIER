# USING INPUT IN DICTIONARIES

"""
A dictinary created by the user where number of entries determines the 
number of key:value pairs the user will input in the dictionary.
"""

num = int(input("Enter the number of entries"))
dict = {input('enter key: '):input("enter value") for _ in range(num)}

print(dict)

# MAKING A FUNCTION FOR THE ABOVE CODE
def create_dict():
    enter_number = int(input("Enter the number of entries")) #enter_number & dictionary are local variables
    dictionary = {input('enter key: '):input("enter value") for _ in range(enter_number)}

    print(dictionary)

create_dict()    

# we can access num1 from within our function as seen below
num1 = int(input("Enter the number of entries"))
def create_dict():
    num2 = num1 #num2 is a local variable while num1 is a global variable
    dictionary = {input('enter key: '):input("enter value") for _ in range(num2)}

    print(dictionary)

create_dict() 