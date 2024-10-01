birthday = (4, 12, 1991)

# print(len(birthday))
# print()

# print(birthday[0])
# print(birthday[1])
# print(birthday[-1])

# print(birthday[10]) IndexError

# birthday[1] = 13 TypeError

addresses = (
    ['Hudson Street', 'New York', 'NY'],
    ['Franklin Street', 'San Francisco', 'CA']
)

# addresses[1] = ["Something Else"] TypeError

addresses[1][0] = "Polk Street"

# print(addresses)

print(dir(birthday)) 
print(birthday.count(4))