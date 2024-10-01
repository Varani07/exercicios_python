# Meu Código

# def reverse(str):
#     count = len(str)
#     if count > 0:
#         print(str[count - 1], end="")
#         reverse(str[:count - 1])

# reverse("python")

# ---------------------------------------------

# Código do professor

# def reverse(str):
#     start_index = 0
#     last_index = len(str) - 1
#     reversed_string = ""

#     while last_index >= start_index:
#         reversed_string += str[last_index]
#         last_index -= 1

#     return reversed_string 

def reverse(str):
    if len(str) <= 1:
        return str
    
    return str[-1] + reverse(str[:-1])

print(reverse("straw"))

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)
    
print(factorial(4))