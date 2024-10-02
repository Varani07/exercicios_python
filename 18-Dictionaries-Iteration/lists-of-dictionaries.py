concert_attendees = [
    {"name": "Taylor", "section": 400, "price paid": 99.99},
    {"name": "Christina", "section": 200, "price paid": 149.99},
    {"name": "Jeremy", "section": 100, "price paid": 0.0}
]
for attendee in concert_attendees:
    for key, value in attendee.items():
        print(f"The {key} is {value}")

# Assign a list of four dictionaries to a "complexity" variable below

# The first and third dictionaries should have two key-value pairs
# For those dictionaries, the keys should be strings and the values should be Booleans

# The second and fourth dictionaries should have three key-value pairs
# For those dictionaries, the keys shoulds be floats and the values should be list of strings. 
# The lists can be of any length.
complexity = [
    {"one": True, "two": False},
    {1.2: ["one", "two"], 1.1: ["three"], 1.9: ["Hello There"]},
    {"one": False, "two": True},
    {1.4: ["four", "five"], 1.5: ["six", "seven"], 1.7: ["There Hello"]}
]