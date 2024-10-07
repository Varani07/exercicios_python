def one():
    return 1

print(type(one))

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b

def calculate(func, a, b):
    return func(a, b)

print(calculate(add, 5, 6))
print(calculate(subtract, 8, 3))

# Define an invoke_thrice function.
# It should accept a single argument (which will be a function)
# In its body, the invoke_thrice function should invoke
# the function that's passed in exactly three times.
def invoke_thrice(func):
    func()
    func()
    func()