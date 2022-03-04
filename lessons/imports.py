"""Examples of importing python."""


from lessons import helpers
#  from lessons import helpers as hp
# from lessons.helpers import powerful <- another verison of importing
#  import names defined globally
from lessons.helpers import powerful, THE_ANSWER

def main() -> None:
    """Entrypoint of programs."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {helpers.THE_ANSWER}")


if __name__ == "__main__":
    main()