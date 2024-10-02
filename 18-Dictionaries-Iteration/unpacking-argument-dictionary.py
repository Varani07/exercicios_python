def height_to_meters(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches * 0.0254

print(height_to_meters(5, 11))

stats = {
    "feet": 5,
    "inches": 11
}
print(height_to_meters(**stats))
# Precisa ser a mesma quantidade com os mesmos nomes(feet, inches)

def plenty_of_arguments(a, b, **kwargs):
    total = a + b
    for value in kwargs.values():
        total += value
    result = total > 100
    return result

# prof cod
def plenty_of_arguments(a, b, **kwargs):
    return a + b + sum(kwargs.values()) > 100