print(3 in [5, 2, 3, 4, 6, 8, 3])

def contains(values, target):
    found = False
    for value in values:
        print(value)
        if value == target:
            found = True
            break
    return found

print(contains([1, 2, 3, 4, 5], 3))