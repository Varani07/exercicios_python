bubble_tea_flavors = [
    ["Honeydew", "Mango", "Passion Fruit"],
    ["Peach", "Plum", "Strawberry", "Taro"],
    ["Kiwi", "Chocolate"]
]

# print(len(bubble_tea_flavors))

# print(bubble_tea_flavors[0])
# print(bubble_tea_flavors[1])
# print(bubble_tea_flavors[-1])

# print(len(bubble_tea_flavors[0]))
# print(len(bubble_tea_flavors[1]))
# print(len(bubble_tea_flavors[2]))

# print(bubble_tea_flavors[2][1])
# print(bubble_tea_flavors[2][2]) IndexError

all_flavors = []

for flavor_pack in bubble_tea_flavors:
    for flavor in flavor_pack:
        all_flavors.append(flavor)

print(all_flavors)

# def nested_sum(list_num):
#     total = 0
#     for lists in list_num:
#         for values in lists:
#             total += values
#     return total

# def fancy_concatenate(list_of_lists):
#     final_string = ""
#     for lists in list_of_lists:
#         if len(lists) == 3:
#             for string in lists:
#                 final_string += string
#     return final_string