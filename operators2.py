# COMPARISON OPERATORS
# example of comparison operators ==, !=, >, <, >=, <=
#These compare two values and return a boolean (TRUE or FALSE)

# Examples
comp1 = 20
comp2 = 40

print(comp1 > comp2) # greater than
print(comp1 < comp2) # less than
print(comp1 >= comp2) # greater or equal to
print(comp1 <= comp2) # less than or equal to
print(comp1 != comp2) # not equal to
print(comp1 == comp2) # equal to

#NOTES
#1. Write comments above the line you intent to comment about and never besides the statements like above
#2. Assignment should be started on Thursday in google classroom
#3. When commenting, follow rules of English Grammar ie fullstops, commas, exclamation marks etc

# LOGICAL OPERATORS
# and (&) - TRUE if both operands are TRUE), or(if atleast one operand is TRUE), not(If the operand is FALSE)
# or(|) - if atleast one operand is TRUE
# not(!) - If the operand is FALSE

log1 = 5
log2 = 6

print((log1 > log2) & (log2 < log1))
print((log1 < log2) or (log2 < log1))

fig1 = 2
not fig1

print(True or True)

# AND
print(True and True) #True
print(False & False) #False
print(True and False) #False
print(False & True) #False

#OR
print(True | True) #True
print(False or False) #False
print(True or False) #True
print(False | True) #True

#NOT
print(not True) #False
print(not False) #True

# MEMBERSHIP OPERATORS (in, not in)

numbers = {20, 30, 40, 50}

print(20 in numbers) #True
print(20 not in numbers) #False

name = 'Ozzy'
print('o' in name) #False because python is case sensitive
print("O" in name) #True