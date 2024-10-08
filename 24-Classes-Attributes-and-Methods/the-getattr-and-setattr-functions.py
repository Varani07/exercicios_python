stats = {
    "name": "BBQ Chicken",
    "price": 19.99,
    "size": "Extra Large",
    "ingredients": ["Chicken", "Onion", "BBQ Sauce"]
}

class Pizza():
    def __init__(self, stats):
        for key, value in stats.items():
            setattr(self, key, value)


bbq = Pizza(stats)
print(bbq.size, bbq.ingredients)

for attr in ["price", "name", "diameter", "discounts"]:
    print(getattr(bbq, attr, "Unkown"))
    # print(getattr(bbq, attr)) AttributeError