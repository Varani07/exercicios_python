def positive_or_negative(number):
    if number > 0:
        return "Positive!"
    elif number < 0:
        return "Negative!"
    else:
        return "Neither! It's zero."
    
print(positive_or_negative(1))
print(positive_or_negative(0))
print(positive_or_negative(-7))

def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "I dont know what you want me to do!"
    
print()
print(calculator("add", 4, 67))
print(calculator("divide", 8, 4))
print(calculator("multiply", 5, 5))
print(calculator("subtract", 6, 3))
print(calculator("hsh", 7, 7)) 