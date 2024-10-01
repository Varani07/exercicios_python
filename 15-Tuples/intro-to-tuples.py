foods = ("Sushi", "Steak", "Guacamole")

print(type(foods))

empty = ()
print(type(empty))

# mystery = (1)
# print(type(mystery))
mystery = 1,
print(type(mystery))

mystery = (1, )
print(type(mystery))

print(tuple(["Sushi", "Steak", "Guacamole"]))
print(tuple(["sushi"]))
print(tuple("sushi"))

# print(tuple(234)) TypeError not iterable

# months = ("September", "October", "November", "December")

# faves = ["Pulp Fiction", "Harry Potter", "Deadpool"]
# movies = tuple(faves)

# numbers_a = (4, 6, 7)
# numbers_b = (1, 1, 1)
# numbers_c = (9, 8, 7)
# all_numbers = (numbers_a,  numbers_b, numbers_c)