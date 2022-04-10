""""""
from __future__ import annotations


class StrArray:
    items: list[str]

    def __init(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        """A Str."""
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray) -> StrArray: 
        """Vectorized concatenation operator."""
        result: list[str] = []
            
            if isinstance(rhs,str):
                for item in self.items:
                    result.append(item + rhs)
            else:
                assert len(self.items) == len(rhs.items)
                for i in range(o, len(self.items)):
                    result.append(self.items[i] + rhs.items[i])
        return StrArray(result)


        # setup a result list of strings that's empty
        # loop through each item in self.items
        #  for each item, append the concatenation of item and rhs to result list
        # return a newly constructed StrArray whose items are result

first: StrArray = StrArray(["Armando", "Brady", "Caleb"])


last: StrArray = StrArray(["Bacot", "Manek, "Love"])
result: StrArray = first + "!"
print(result)
print(first + last)