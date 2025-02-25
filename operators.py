# OPERATORS IN PYTHON
# An Operator is a character or a special symbol that tells a computer what to do with an operand(value).

num = 100 # The equal sign is an operator and tells CPU to do something with the value 100. 
#100 in this case is our operand whlist the operator is =

#TYPES OF OPERATORS IN PYTHON
# 1. Arithmetic Operators e.g (+, -, /, *, % modulo ie remainder after division, // called floor division and rounds up to nearest smaller whole number e.g 3.5 will be 3, ** raised to the power)
# 2. Logical Operators e.g (and(TRUE is both operands are TRUE), or(if atleast one operand is TRUE), not(If the operand is FALSE))
# 3. Bitwise Operators (&- Bitwise AND, |- Bitwise OR, - Bitwise NOT, ^ - Bitwise XOR, >> Bitwise right shift, << Bitwise left shift)
# 4. Membership Operators (in - True if value/variable is 'FOUND' in sequence, not in - True if value/variable is 'NOT FOUND' in sequence)
# 5. Assignment Operators e.g (=, +=, -=, *=, /=, %=, **=)
# 6. Comparison Operators e.g (==, !=, >, <, >=, <=)
# 7. Identity Operators (is - True if operands are 'identical', is not - True if operands are 'not identical')

#ARITHMETIC OPERATORS

num1,num2 = 30,200

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2) #returns a float value
print(num1 // num2) #floor division returns a int ie rounds to nearest small whole number
print(num1 % num2) #modulus returns the remainder
print(num2**2) #num2 raised to the power 2

#ASSIGNMENT OPERATORS

num3 = 10 # = is an assignment
num3 += 10 #+=(means additional assignment) num3 is now num3 + 10
print(num3)

num3 -= 10 #+=(means subtraction assignment) num3 is now num3 - 10
num3

num3 *= 5 #+=(means multiplication assignment) num3 is now num3 * 5
num3

num3 /= 2 #+=(means division assignment) num3 is now num3 / 2
num3

num3 %= 6 #+=(means division assignment) num3 is now num3 % 6
num3

num3 **= 2 #+=(means division assignment) num3 is now num3 ** 2
num3