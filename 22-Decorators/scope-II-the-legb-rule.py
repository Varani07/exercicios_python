# Global Escope
# x = 25 

def outer():
    # Enclosing Function Escope
    # x = 10

    def inner():
        # Local Escope
        # x = 5
        return len
    
    return inner()

print(outer()("python"))