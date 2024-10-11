def divide_five_by_number(n):
    try:
        calculation = 5 / n
    except ZeroDivisionError:
        return "You can't divide by zero!"
    except TypeError as e:
        return f"No dividing by invalid objects! {e}"

    return calculation

print(divide_five_by_number(0), " | ", divide_five_by_number(10))
print(divide_five_by_number("Nonsense"))

print()

def divide_five_by_number(n):
    try:
        calculation = 5 / n
    except (ZeroDivisionError, TypeError) as e:
        return f"Something went wrong, the error was {e}"

    return calculation

print(divide_five_by_number(0), " | ", divide_five_by_number(10))
print(divide_five_by_number("Nonsense"))