#STATIC FUNCTIONS
#These are hard coded into the function just like we've been doing all this while
def add():
    num = 5
    num1 = 10
    return num + num1

print(add())

#DYNAMIC FUNCTIONS
#they expect values upon calling the function
#They allow you to define variables in the function with the function name

def add1(num,num1): # values within() are called arguements
    return num + num1

add1(50,40) #won't see anything because return stores values until we say print
print(add1(50,40)) #we enter our arguements within the () of our dynamic function
print(add1(5,10))