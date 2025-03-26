#inheritance is when 2 individual classes share the same properties.
# inheritance is the ability of a sub/child/derived-class to take on one or more attributes of a super/parent/base class

class Animal():
    name = ""
    color = ""
    weight = 50
    owner = ""

# a method is a function within a class
# The statements you write in a method in this case function are refered to as behaviours

    def sound(self):
        print(" I bark")

# Creating an object from our class
horse = Animal()
horse.sound() #we a calling our method here