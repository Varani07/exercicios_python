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
print(bbq.size)
stats_to_delete = ["size", "parameter", "spiciness", "ingredients"]

for stat in stats_to_delete:
    if hasattr(bbq, stat):
        delattr(bbq, stat)

# print(bbq.size) AttributeError - Atributo deletado com sucesso!