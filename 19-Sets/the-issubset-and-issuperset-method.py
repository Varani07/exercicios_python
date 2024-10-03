a = {1, 2, 3, 4}
b = {1, 2, 3, 4, 5, 6}

print(a.issubset(b), a < b)
print(a.issuperset(b), a > b)
print(b.issuperset(a), b > a)
print(b >= a)