"""An oracle that predicts the future."""

from random import randint

input("Ask a yes/no question: ")

response: int = randint(0, 3)


if response == 0:
    print("Most Defintley")
elif response == 1:
    print ("highly likely")
elif response == 2:
    print("Ask again later")
else:
    print("no way, not a chance")
