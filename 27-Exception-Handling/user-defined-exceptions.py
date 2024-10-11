class NegativeNumbersError(Exception):
    """One or more inputs are negative"""
    pass

def add_positive_numbers(a, b):
    try:
        if a <= 0 or b <= 0:
            raise NegativeNumbersError
        return a + b
    except NegativeNumbersError:
        return f"Shame on you, not valid!"
    
print(add_positive_numbers(3, 5))
print(add_positive_numbers(-3, 9))