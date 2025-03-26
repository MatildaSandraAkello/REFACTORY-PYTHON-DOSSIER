# OBJECT ORIENTED PROGRAMING

"""
1. OOP is a programming concept(paradigm or belief or arrangement) that advocates for writing software based on real life objects.
2. OOP is object focused
3. Class, Object, Properties(attributes, characteristics, features)
4. Methods
5. Constructors
6. Principles of object oriented programming (abstraction, encapsulation, inheritance, polymorphism)
7. Overloading & Overriding
8. Objects are gotten from classes ie they are classified meaning they belong somewhere
9. An object is gotten from a class
10. Classes are identified in singular not plural. It's the objects that are identified in plural
11. A Class is a blue print of an object ie blue print means the original format of something
12. An Object is an instance of a class
13. Classes defines the attribute, features, characteristics of it's objects
14. Basically a class is a blue print / master plan/ original format/ skeleton
14. What we used to call variables are know going to be called properties,attributes, features and characteristics because we are defining a thing.
15. An object should fulfill all properties of a class.
16. We can have an class with no objects because we create a class first before its objects
"""


student = ['Matilda', 'Sandra', 'Akello']
student1 = {'name':'Matilda', 'Gender':'Female', 'School':"Private", "Age":25}

#A CLASS NAME SHOULD START WITH A CAPS LETTER
# class with no objects
class Laptop():
    pass

#creating our class with it's attributes
class Food():
    #attributes/properties/features of our class
    name = ""
    taste = ""
    calories = 0
    price = 0
    value = ""

#Creating objects out of our class Food above
matooke = Food()

matooke.name = "Matooke"
matooke.taste = "Sweet"
matooke.calories = 0
matooke.price = 25000
matooke.value = "One"

rice = Food()

rice.name = "Rice"
rice.taste = "Salty"
rice.calories = 3
rice.price = 4000
rice.value = "1 Kg"

print(rice.name)
