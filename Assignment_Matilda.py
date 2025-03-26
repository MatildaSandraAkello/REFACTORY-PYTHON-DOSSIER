#Assinging variable some_string with a string value then printing it's data type
some_string = 'Python is fun' 
print(type(some_string))

#Assigning multiple variables a,b,c values 5, 3.2 'Hello'
a, b, c = 5, 3.2, 'Hello'

# Displaying the values of our variables a, b, c
print(a)  # This prints the integer number 5
print(b)  # This prints the float number 3.2
print(c)  # This prints the string 'Hello'

#Assigning variable num1, an integer value of 5
num1 = 5

# Displaying the data type of num1
print(num1, 'is of type', type(num1))

#Assigning Variable num2, a float value 2.0
num2 = 2.0

# Displaying the data type of num2
print(num2, 'is of type', type(num2))

#Assigning Variable num3, a complex value 1+2j
num3 = 1+2j

# Displaying the data type of num3
print(num3, 'is of type', type(num3))

#Assinging a variable called languages with a list of string values
languages = ["Swift", "Java", "Python"]

# Displaying value at index position 0 in our list called languages
print(languages[0])   # 'Swift'

# Displaying value at index position 2 in our list called languages
print(languages[2])   # 'Python'

# Assigning a variable called product, with a tuple storing string and float values
product = ('Microsoft', 'Xbox', 499.99)

# Displaying value at index position 0 in our tuple called product
print(product[0])   #'Microsoft'

# Displaying value at index position 1 in our tuple called product
print(product[1])   #'Xbox'

# Assigning a variable called capital_city with a dictionary storing string values
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}

# Displaying our dictionary, capital_city
print(capital_city)

# Assigning a variable called student_id with a dictionary storing integer values
student_id = {112, 114, 116, 118, 115}

# Displaying our dictionary, student_id
print(student_id)

# Displaying the data type of student_id
print(type(student_id))

# Assigning a variable called fruits, with a list of string values
fruits = ["apple", "mango", "orange"] 

#Displaying our list, called fruits
print(fruits)

# Assigning a variable called numbers with a tuple storing integers
numbers = (1, 2, 3) 

# Displaying our tuple, numbers.
print(numbers)

# Assigning a variable, alphabets with a dictionary
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 

# Displaying our dictionary, alphabets
print(alphabets)

# Assigning a variable, vowels with a set storing string values then printing out our set.
vowels = {'a', 'e', 'i' , 'o', 'u'} 
print(vowels) 

# Assigning a variable student_id with a set of interger values
student_id = {112, 114, 116, 118, 115}

# Displaying our set, student_id
print(student_id)

# display type of student_id
print(type(student_id))

# Assign a variable product, storing string values and float value
product = ('Microsoft', 'Xbox', 499.99)

# Displaying value in our tuple at index position 0.
print(product[0])   # 'Microsoft'

# Displaying value in our tuple at index position 1.
print(product[1])   # Xbox


# Assigning variables a and b with int values.
a = 7
b = 2

# Displaying the sum of variables a and b.
print ('Sum: ', a + b)  

# Displaying the differnce of variables a and b.
print ('Subtraction: ', a - b)   

# Displaying the product of a and b.
print ('Multiplication: ', a * b)  

# Displaying the quotient of a and b.
print ('Division: ', a / b) 

# Displaying the floor division value of a and b.
print ('Floor Division: ', a // b)

# Displaying the modulo value of a and b.
print ('Modulo: ', a % b)  

# Displaying the power of a and b.
print ('Power: ', a ** b)   


# Assigning variable a with an int value
a = 10

# Assigning variable b with an int value
b = 5 

# Assigning variable 'a' with a new value which is the sum of a and b
a += b      # a = a+b
print(a)
# Output: 15


# Displays a False because variable a is not equal to b.
print('a == b =', a == b)

# Displays a True because variable a is not equal to b.
print('a != b =', a != b)

# Displays a True because variable a is greater than b.
print('a > b =', a > b)

# Displays a False because variable a is less than b.
print('a < b =', a < b)

# Displays a True because variable a is greater than or equal to b.
print('a >= b =', a >= b)

# Displays a False because variable a is less than or equal to b.
print('a <= b =', a <= b)

# Displays a False because one of the conditions is False
print((a > 2) and (b >= 6)) 

# logical operator AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical operator NOT
print(not True)          # False

# Assigning variables with values
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Identity operator IS NOT
print(x1 is not y1)  # False

# Identity operator IS
print(x2 is y2)  # True

# Identity operator IS
print(x3 is not y3)  # False

# Assigning variable called message with a string value.
message = 'Hello world'

# Assigning variable dict with a dictionary
dict1 = {1:'a', 2:'b'}

# Membership Operator IN
print('H' in message)  # True

# Membership Operator NOT IN
print('hello' not in message)  # True

# Membership Operator IN
print(1 in dict1)  # True

# Membership Operator IN
print('a' in dict1)  # False
