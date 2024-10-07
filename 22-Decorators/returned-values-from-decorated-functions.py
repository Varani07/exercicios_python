def be_nice(fn):
    def inner(*args, **kwargs):
        print("Nice to meet you!")
        result = fn(*args, **kwargs)
        print("Have a nice day!")
        return result

    return inner

@be_nice
def complex_business_sum(a, b):
    return a + b

print(complex_business_sum(a = 3, b = 5))