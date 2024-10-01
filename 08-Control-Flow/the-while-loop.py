# count = 0

# while count <= 5:
#     print(count)
#     count += 1

# print(count)

invalid_number = True

while invalid_number:
    user_value = int(input("Please enter a number above 10: "))
    if user_value > 10:
        print("Hey thats great!")
        invalid_number = False
    else:
        print("That doesnt fit.")