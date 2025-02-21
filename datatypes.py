#DATA TYPES IN

#Data types specify data that can be stored inside a variable
#Data types in pyhton include:
# 1. Numeric - can be int, float,complex & holds numeric values
# 2. String "" or '' holds a sequence of characters
# 3. mapping - here we have dictionaries {} & they hold key-value pairs forms of a variable
# 4. Boolean - holds either TRUE or FALSE
# 5. set - can be just a set or a frozen set & hold a collection of unique items that are unordered
# 6. sequence - can be a tuple (), list[], or range & holds a collection of items
num = 200 #int
print(type(num))
num2 = 200.0 #float
print(type(num2))
num3 = 1+ 2j #complex
print(type(num3))
num4 = "word" #string
print(type(num4))
word = 'Hello World'
print(type(word))
print(word[1])
print(word[0])
print(word[-1])

num5 = 1 + 6j
print(num5, "is of type", type(num5))
num6 = 5.2
print(num6, "is of type", type(num6))
num7 = 'Matilda'
print(num7, "is of type", type(num7))