if 5 < 7 and "rain" == "rain":
    print("Both conditions are true!")

if 5 < 7 and "rain" == "fire":
    print("this will not print")

if "rain" == "fire" and 5 < 7:
    print("this will not print")

if "rain" == "fire" and 5 < 3:
    print("this will not print")

value = 95

# if value > 90 and value < 100:

if 90 < value < 100:
    print("This is a shortcut for the win!")