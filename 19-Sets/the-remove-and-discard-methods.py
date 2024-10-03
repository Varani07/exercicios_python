names = {"Thabata", "Matheus", "Lucas", "Junior"}
print(names)
names.remove("Thabata")
print(names)
# names.remove("Alcina") KeyError
names.discard("Alcina") # Não muda nada se o elemento não existir.
print(names)
names.discard("Matheus")
print(names)