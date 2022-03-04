"""Demonstration of dictionary capabilites."""

# Declaring the type of a dictionrary
schools: dict[str, int]

# intialzie to an empty dcitionary
schools = dict()

# set a key--value parining in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# print a dictionary literal reprsentation
print(schools)

# Access a value by its key -- "lookup" needed to use the single quotes
print(f"UNC has {schools['UNC']} students")

# remove a key value pair from a dictionary
#  by its key, mainly referenced by value
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(is_duke_present)


if "Duke" in schools:
    print("key found")

# update / reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# inverting a dictionary
invert_schools: dict[int,str]
invert_schools = dict()
invert_schools [19400] = "UNC"


# demonstration of dictionary literals

# empty dictionary literal
schools = {} # same as dict()
print(schools)

schools = {"UNC": 19400, "Duke": 6717}
print (schools)

# what happens when a key does not exist
print(schools["UNC"])
# python -m lessons.dictionaries