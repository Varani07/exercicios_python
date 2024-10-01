temperature = [40, 28, 52, 66, 35]
temperature.sort()
temperature.reverse()
print(temperature)

coffees = ["Latte", "Espresso", "Macchiato", "Frappucino"]
coffees.sort()
print(coffees)

coffees = ["Latte", "espresso", "macchiato", "Frappucino"]
coffees.sort()
print(coffees)

# dont mutate
coffees = ["Latte", "espresso", "macchiato", "Frappucino"]
print(sorted(coffees))