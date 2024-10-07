def outer():
    candy = "Snickers"

    def inner():
        return candy
    
    return inner

print(outer())

the_func = outer()
print(the_func())