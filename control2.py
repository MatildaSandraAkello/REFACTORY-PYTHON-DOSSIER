number = int(input("input first number"))

if number >= 0:
    print("Positive Number")
else:
    print("Negative Number")    

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#Loops are very expensive interms of memory because every time it loops it creates a new memory.
#In programming avoid loops as much as possible
# Is also memory expensive
# Loops are sensitive if you don't break them they can crash your computer

#FOR LOOPs
fruits = ["apple", "banana", "mangoes", "berry"]

for item in fruits:
    print(item)
    if item == "banana":
        break

"""
You can either use 'pass' or 'break' to terminate the loop once the condition is met
"""
for item in fruits:
    print(item)
    if item == "banana":
        pass


#WHILE LOOPs
# Is also memory expensive
# Loops are sensitive if you don't break them they can crash your computer
count = 5

while count <= 10:
    print(count)
    count += 1
    print("the value of count is:", count)
    if count == 10:
        break
      