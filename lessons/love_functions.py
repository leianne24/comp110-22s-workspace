"""Love me tender *music noises*."""


def love(name: str) -> str:
    """Given a name as a paramater, returns a tender loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    i: int = 0
    love_note = ""
    while i < n:
        #concatenation
        love_note += love(to) + "\n"
        i += 1 # i = i + 1
        #i + 1 would not store the 1 in the 1, it wouldn't change anything
    return love_note

    # the "\n" isn't doing what I think it's supposed to be doing. We have to print it to get rid of those. 