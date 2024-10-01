errands = ["Go to gym", "Grab lunch", "Get promoted at work", "Sleep"]

print(enumerate(errands))

for index, errand in enumerate(errands, 1):
    print(f"{index}: {errand}")

for index, errand in enumerate(errands):
    print(f"{index + 1}: {errand}")