#SEQUENCE DATA TYPE IN PYTHON
num1, num2, num3 = 100, 300, 500 #the problem with this arrangement is that it wastes memory since each variable will be a separate memory. Sequence helps us handle this problem
numbers = [100, 300, 500] #now in this single memory location it stores 3 values
numbers1 = [num1, num2, num3] #this too now stores values of line 2 in one memory location
#values stored in [] are called LISTS, and stored in one single memory location ie in one variable
# A list can store values of different data types in one variable.
# Lists store single values ie iformation about one thing unlike dictonaries that hold say a student's details  
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
# Tuples are read only, but can also hold different data types 
mytuple = (100, 300, 500)
print(type(mytuple))
print(mytuple[0])

mytuple2 = (100, [200,300,400], "Matilda", 'Sandra')
print(mytuple2)
print(mytuple2[1])

#Key-Value pairs stored in curly braces{} are Called DICTIONARIES,a dictionary is an ordered collection of key-value paired items
capital_city = {'Nepal':'Kathmandu', 'Italy':'Rome', 'England':'London'}
print(capital_city)
print(type(capital_city))

#Dictonary option 2 arrangement
capital_city2 = {'Nepal':'Kathmandu',
'Italy':'Rome',
'England':'London'
}
capital_city2

#Dictonary option 3 arrangement housing strings intergers and lists
capital_city2 = {
1 : 'Matilda',
2 : "Sandra",
3 : [24,26,30],
4 : 50
}
capital_city2[3] #we use keys to access the values and not values to access the keys!

#Values only(not key:value pairs) stored in curly braces{} are Called SET, These are unordered collection of unique items & immutable (unchangeable)
student_id = {112, 114, 116, 118, 115}
student_id
type(student_id)

names = {'Matilda', "Sandra", "Akello"}
print(names)
print(type(names))
#FACT: A Set is an unordered collection that does not support accessing elements by a specific position or index. The concept of indexing does not align with the nature of a Set