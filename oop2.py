class animal():
    name = ""
    kind = ""
    sound = ""
    edible = ""

# The dot operator is used to access the name of a property/Xtics of an object
# An object can take one or more properties
cow = animal()

cow.name = "cow"
cow.kind = "domestic"
cow.sound = "moo"
cow.edible = "beef"

# Printing only edible attribute
print(cow.edible)

# Printing all properties of the cow at once 
print(f"cow: {cow.name} - {cow.kind} - {cow.sound}, {cow.edible}")

#Abstraction is the ability to ignore something and concentrate on something particular
#All objects have a level of abstract