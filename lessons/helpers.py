"""Demonstrate defining a module imported elsewhere."""

THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2,10))
    print("helpers.py run as a module")

def powerful(x: float, n: float) -> float:
    """Raise to the power of n."""
    return x ** n

# idiom for making a module able to run as a program
# or have its global defintions imported elsewhere
if __name__ == "__main__":
    main()
else:
    print(f"helpers.py was imported: {__name__}")
    # it is not idiomatic to have an elese branch