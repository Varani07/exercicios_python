print(set([1, 2, 3]))
print(set([1, 2, 3, 5, 4, 3, 8, 2, 1]))

print(set((1, 2)))
print(set((1, 2, 2, 1)))

print(set("abc"))
print(set("aabbcc"))

print(set({"key": "value"}))

philosophers = ["Plato", "Socrates", "Aristotle", "Pythagoras", "Socrates", "Plato"]
philosophers_set = set(philosophers)
philosophers = list(philosophers_set)
print()
print(philosophers)