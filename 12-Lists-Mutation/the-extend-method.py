mountains = ["Mountain Everest", "K2"]
print(mountains)
print()

mountains.extend(["Kangchenjunga", "Lhotse", "Makalu"])
print(mountains)
print()

extra_montains = ["Cho Oyu", "Dhaulagiri"]
mountains.extend(extra_montains)
print(mountains)
print()

mountains.extend([])
print(mountains)
print()

steaks = ["Tenderloin", "New York Strip"]
more_steaks = ["T-Bone", "Ribeye"]

my_meal = steaks + more_steaks

print(my_meal)
print()

print(steaks)
print()

print(more_steaks)
print()

steaks += more_steaks
print(steaks)