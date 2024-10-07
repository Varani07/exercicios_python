def be_nice(fn):
    def inner():
        print("Nice to meet you!")
        fn()
        print("Have a nice day!")

    return inner

@be_nice
def complex_business_logic():
    print("Something Complex")
@be_nice
def another_fancy_function():
    print("Alright!")

# result = be_nice(complex_business_logic)
# result()

# be_nice(complex_business_logic)()

complex_business_logic()
another_fancy_function()