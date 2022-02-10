"""A list game: exapmples of using lists in a simple game thing?"""

from random import randint

randint
rolls: list[int] = list() 

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)

#removing an item from the list by its index, alwasy removes final item
rolls.pop(len(rolls) - 1)
print(rolls)

#sum the values of our rolls
i: int = 0
sum: int = 0
while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1
print(f"Total score: {sum}")


# manually making list: List literal syntax
# rolls = [10, 20, 30]



# rolls.append(randint(1, 6)) #this is a method call: we have our list, the function, and use the number 1 is the argument
# rolls.append(randint(1, 6))
# 
# print(rolls)

# #accessing indivual items
# print(rolls[0])
# print(rolls[1])

# #accessing the lenth of a list (number of items)
# print(len(rolls))
# #finding the last part of our lsit, -1 accounts for the zero index
# print(rolls[len(rolls) - 1])