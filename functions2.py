# return - returns a value / exposes value/ allows the value of a function to be accessed outside the function
# return is also used when one function wants to access a value from another function ie if you intend to use a value from one function in another
# return statement marks the end of execution of a function

def add():
    var1 = 23
    var2 = 45
    return var1 + var2

print(add())

my_num = add()
my_num

def sub():
    var1 = 23
    var2 = 45
    return var2 - var1

print(sub())

def both():
    return sub() + add()

print(both())

def add1():
    var3 = int(input("Please enter your first number"))
    var4 = int(input("Please enter your second number"))

    return var3 + var4

def sub1():
    var3 = int(input("Please enter your first number"))
    var4 = int(input("Please enter your second number"))
    
    return var3 + var4

def both1():
    return sub1() + add1()

print(both())

"""
Uptill now the functions we've studied are called Static function (those with hard coded values)

"""
