from unittest.mock import Mock

pizza = Mock()
print(pizza)
print(type(pizza))
# pizza.size = "Large"
# pizza.price = 10.00
# pizza.toppings = ["Pepperoni", "Mushroom", "Sausage"]
pizza.configure_mock(
    size = "Large",
    price = 19.99,
    toppings = ["Pepperoni", "Mushroom", "Sausage"]
)
print(pizza.size, pizza.price, pizza.toppings)


# print(pizza.anything)
# print(pizza.anything.we.want)

print(pizza.cover_with_cheese())
print(pizza.cover_with_cheese())