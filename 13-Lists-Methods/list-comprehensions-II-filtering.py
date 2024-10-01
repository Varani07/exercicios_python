print(["abcdefghijklmnopqrstuvwxyz".index(char) for char in "donut"])
range(20)
print([number/2 for number in range(20)])

donuts = [
    "Bostom Cream",
    "Jelly",
    "Vanilla Cream",
    "Glazed", 
    "Chocolate Cream"
]

# creamy_donuts = []

# for donut in donuts:
#     if "Cream" in donut:
#         creamy_donuts.append(donut)
# print(creamy_donuts)

creamy_donuts = [donut for donut in donuts if "Cream" in donut]
print(creamy_donuts)

print([len(donut) for donut in donuts if "Cream" in donut])

print([donut.split(" ")[0] for donut in donuts if "Cream" in donut])

# MEU CÓDIGO
# values = ["3.14", "9.99", "567.324", "5.678"]
# floats = [float(number) for number in values]

# name = "Boris"
# letters = [char*3 for char in name]

# elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
# lengths = [len(string) for string in elements]

# def destroy_elements(list1, list2):
#     new_list = [element for element in list1 if element not in list2]
#     return new_list