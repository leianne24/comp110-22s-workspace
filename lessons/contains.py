"""example of a function that searches through a list."""


def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Kevin Bacon", "turtle"]))
# define a function named contians
# two parameters:
#   1. needle - the string we're searching for
#   2. haystack - the list we're searching through
def contains(needle: str, haystack: list[str]) -> bool:
 
# Algrothim
# for each item in the haystack
#   test if it is equal t the needlie
#   if so, return true
    for item in haystack:
        if item == needle:
            return True
# after testing all tiems, return false, because not found
# Returns true if needles in the haystack, False otherwise

    return False
if __name__ == "__main__":
    main()
else: 
    print (__name__)
# from lessons.contains import contains