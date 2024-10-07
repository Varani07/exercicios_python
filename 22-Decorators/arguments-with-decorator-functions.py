def be_nice(fn):
    def inner(*args, **kwargs):
        print("Nice to meet you!")
        print(args)
        print(kwargs)
        fn(*args, **kwargs)
        print("Have a nice day!")

    return inner

@be_nice
def complex_business_logic(stakeholder, position):
    print(f"Something Complex for our {position} {stakeholder}")

# complex_business_logic("Matheus") TypeError
# complex_business_logic("Matheus", "CEO") 
# complex_business_logic(stakeholder="Matheus", position="CEO") 
complex_business_logic("Matheus", position="CEO")