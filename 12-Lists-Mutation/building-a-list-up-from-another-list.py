powerball_numbers = [4, 8, 15, 16, 23, 42]

def squares(numbers):
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    return squares

print(squares(powerball_numbers))

def convert_to_float(numbers):
    float_numbers = []
    for number in numbers:
        float_numbers.append(float(number))
    return float_numbers

print(convert_to_float(powerball_numbers))

def even_or_odd(numbers):
    bool_list = []
    for number in numbers:
        if number % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list

print(even_or_odd(powerball_numbers))