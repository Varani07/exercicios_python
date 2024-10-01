flight_prices = {
    "Chicago": 199,
    "san Francisco": 499,
    "Denver": 295
}

print(flight_prices["Chicago"])
# print(flight_prices["Seatle"]) KeyError

gym_membership_packages = {
    29: ["Machines"],
    49: ["Machines", "Vitamin Supplements"],
    79: ["Machines", "Vitamin Supplements", "Sauna"]
}

print(gym_membership_packages[49])

print(gym_membership_packages.get(100, ["Basic Dumbbells"]))
print(gym_membership_packages.get(100))