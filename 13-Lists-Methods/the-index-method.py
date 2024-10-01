pizzas = ["Mushroom", "Pepperoni", "Sausage", "Barbecue Chicken", "Sausage", "Pepperoni"]

print(pizzas.index("Barbecue Chicken"))
print(pizzas.index("Pepperoni"))
print(pizzas.index("Sausage"))
# print(pizzas.index("Olives")) ValueError

if "Olives" in pizzas:
    print(pizzas.index("Olives"))

print()

print(pizzas.index("Pepperoni", 2))
print(pizzas.index("Sausage", 3))

# def encrypt_message(message):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted = ""
#     for letter in message:
#         encrypted_letter_idx = (alphabet.index(letter) + 2) % 26
#         encrypted += alphabet[encrypted_letter_idx]
#     return encrypted