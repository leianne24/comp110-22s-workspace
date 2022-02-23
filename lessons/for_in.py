"""An example of for in syntax."""


names: list[str] = ["Adina", "Leia", "Shane", "Sam"]
# Example of iterating through names using a while loop
print("While output: ")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

print("for...in output: ")
# the following for in loop does the same as the while loop above
for name in names:
    print(name)