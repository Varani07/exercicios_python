print("erm" in "watermelon")
print("z" in "watermelon")
print("z" not in "watermelon")

print()

print(10 in [10, 20])

print()

pokemon = {
    "Fire": ["Charmander", "Charmeleon", "Charizard"],
    "Water": ["Squirtle", "Warturtle", "Blastoise"],
    "Grass": ["Bulbasaur", "Venusaur", "Ivysaur"]
}

print("Fire" in pokemon)
print("Grass" in pokemon)
print("fire" in pokemon)
print("Electric" in pokemon)
print("Electric" not in pokemon)

if "Zombie" in pokemon:
    print(pokemon["Zombie"])
else:
    print("The category of Zombie doesnt exist!")