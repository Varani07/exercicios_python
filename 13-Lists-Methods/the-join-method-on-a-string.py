address = ["500 Fifth Avenue", "New York", "NY", "10036"]


print(", ".join(address))
print("".join(address))

print("-".join(["555", "123", "4567"]))
print("***".join(["555", "123", "4567"]))

# MEU CÓDIGO
# def word_lengths(string: str) -> list:
#     list_lengths = []
#     list_strings = string.split(" ")
#     for word in list_strings:
#         list_lengths.append(len(word))
#     return list_lengths


# def cleanup(list_string: list) -> str:
#     nova_lista = []
#     for item in list_string:
#         novo_item = item.strip()
#         if novo_item != "":
#             nova_lista.append(item)
#     all_string = " ".join(nova_lista)
#     return all_string

# CÓDIGO DO PROFESSOR
# def cleanup(list_string: list) -> str:
#     nova_lista = []
#     for item in list_string:
#         if item.isspace() or len(item) == 0:
#             continue
#         nova_lista.append(item)
#     all_string = " ".join(nova_lista)
#     return all_string