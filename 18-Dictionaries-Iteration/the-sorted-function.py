numbers = [5, 9, 4, 0, 1, 4, 7, 9]
print(sorted(numbers))
print(numbers)

salario = {
    "Adm": 20,
    "AdmSup": 100,
    "tec": 10,
    "bts": 5
}

print(sorted(salario))
print(salario)
print()

wheel_count = {
    "truck": 2,
    "car": 4,
    "bus": 8
}

for vehicle, count in sorted(wheel_count.items()):
    print(f"The next vehicle is a {vehicle} and it has {count} wheels.")