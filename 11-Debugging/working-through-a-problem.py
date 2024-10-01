# values = [1, 2, 3, 4, 5]

# def multiply_element(numbers):
#     total = 0
#     for index, num in enumerate(numbers):
#         pass
#         total += num * (index - 1)
#     return total

# print(multiply_element(values))

values = [1, 2, 3, 4, 5]

def multiply_element(numbers):
    total = 0
    for index, num in enumerate(numbers):
        total += num * (index - 1)
    return total

print(multiply_element(values))