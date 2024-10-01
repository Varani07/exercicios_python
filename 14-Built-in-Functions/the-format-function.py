number = 0.123456789

print(format(number, "f"))
print(type(format(number, "f")))

print(format(number, ".2f"))
print(format(number, ".1f"))
print(format(number, ".3f"))

print(format(0.5, ".2%"))
print(format(0.5, ".0%"))

print(format(12345678, ","))
print()

values = [3.45, 5.67, 7.89]

# list comprehension:

new_list = [number ** 2 for number in values]
print(new_list)

# map function:

new_list2 = list(map(lambda num: num ** 2, values))
print(new_list2)