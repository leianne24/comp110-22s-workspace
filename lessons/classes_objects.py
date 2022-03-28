"""Example of a class and obsject instantiation."""


# remember to make it capital
class Pizza:
    """Models the idea of a Pizza."""

    # Attribute Defintions
    size: str
    toppings: int
    extra_cheese: bool = False

    def price(self, tax: float) -> float:
        """This will calculate the price of a Pizza."""
        total: float = 0.0
        if self.size == "large": 
            total += 10.0
        else:
            total += 8.0
        
        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0

        total += tax

        return total

    def __init__(self, size: str, toppings: int, extra_cheese: bool):
        """Constructor definition for intialztion of attrinutes."""
        self.size = size
        self.toppings = toppings
        self.extra_cheese = extra_cheese


a_pizza: Pizza = Pizza("large", 3)
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${(a_pizza.price(1.05))}")
# This is a method call: is it valid?

another_pizza: Pizza = Pizza("small", 0)