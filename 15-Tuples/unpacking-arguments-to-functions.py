employee = ("Bob", "Johnson", "Manager", 50)

first_name, last_name, *details = employee

print(first_name)
print(last_name)
print(details)

*names, position, age = employee

print(names)
print(position)
print(age)

first_name, *details, age = employee

print()
print(first_name)
print(details)
print(age)

first_name, last_name, position, *details = employee
print(details)
print()
# ---------------------------------------------------

def accept_stuff(*args):
    print(type(args))
    print(args)

accept_stuff(1)
accept_stuff(1, 2, 5)
accept_stuff()

def my_max(*numbers, nonsense):
    print(nonsense)
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

print(my_max(99, 1, 6, 8, 4, 9, 22, 1, -9, nonsense=76))
print()
# ---------------------------------------------------

def product(a, b):
    return a* b

print(product(3, 5))

numbers = [3, 5]
numbers = (3, 5)

print(product(*numbers))