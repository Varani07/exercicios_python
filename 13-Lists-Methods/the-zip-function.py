breakfasts = ["Eggs", "Cereal", "Banana"]
lunchs = ["Sushi", "Chicken Teriyaki", "Soup"]
dinners = ["Steak", "Meatballs", "Pasta"]

# print(zip(breakfast, lunch, dinner))
# print(list(zip(breakfast, lunch, dinner)))

for breakfast, lunch, dinner in zip(breakfasts, lunchs, dinners):
    print(f"My meal for today was {breakfast} and {lunch} and {dinner}.")
    print()