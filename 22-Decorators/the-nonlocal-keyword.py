def outer():
    name = "Matheus"

    def inner():
        nonlocal name
        name = "Thabata"

    inner()

    return name

print(outer())