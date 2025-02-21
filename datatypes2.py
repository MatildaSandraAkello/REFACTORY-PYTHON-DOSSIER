#SEQUENCE DATA TYPE IN PYTHON
num1, num2, num3 = 100, 300, 500 #the problem with this arrangement is that it wastes memory since each variable will be a separate memory. Sequence helps us handle this problem
numbers = [100, 300, 500] #now in this single memory location it stores 3 values
numbers1 = [num1, num2, num3] #this too now stores values of line 2 in one memory location
#values stored in [] are called LISTS, and stored in one single memory location ie in one variable
numbers2 = []
things = [100, "Hello", 300.0, True, [1, 2, 3]]
print(type(numbers))
print(numbers[2])
print(things[1])
print(things[-1])
print(things[-1][0])
print(things[4][-2])
trouble = [20, [30, [100, 20, [500]]]]
print(trouble[1][1][2][-1])
trouble.append(40) #append adds value at the end of the list
print(trouble)
trouble.pop() #removes the value added
print(trouble)

#Values stored in parethensis () are Called TUPLES, they are immutable ie read only sequence, we can only access values in a tuple but not modify
mytuple = (100, 300, 500)
print(type(mytuple))