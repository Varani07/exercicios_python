f_set = frozenset([1, 2, 3, 4, 5, 2])
print(f_set)

# f_set.add(6) AttributeError

regular_set = {1, 2, 3, 4}
# print({regular_set: "Some Value"}) TypeError
print({f_set: "Some Value"})