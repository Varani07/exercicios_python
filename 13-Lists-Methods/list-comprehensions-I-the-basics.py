numbers = [3, 4, 5, 6, 7]
# squares = []

# for number in numbers:
#     squares.append(number ** 2)

# print(squares)
# print(number)

squares = [number ** 2 for number in numbers]
print(squares)
# print(number) NameError

rivers = ["Amazon", "Nile", "Yangtze"]
print([len(river) for river in rivers])

expressions = ["lol", "rofl", "lmao"]
print([string.upper() for string in expressions])

decimals = [4.87, 4.95, 9.56, 10.67]
print([int(decimal) for decimal in decimals])