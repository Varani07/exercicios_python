import copy

# a = [1, 2, 3]

# b = a[:]

# print(a == b, a is b)

# c = a.copy()
# print(a == c, a is c)

# d = copy.copy(a)
# print(a == d, a is d)

numbers = [2, 3, 4]
a = [1, numbers, 5]

b = a[:]
b = a.copy()
b = copy.copy(a)
b = copy.deepcopy(a)

print(a == b, a is b)
print(a[1] is a[1])

b[1].append(200)
a[1].append(100)
print(a, b)