precos = {
    "Suco": 5,
    "Sandubao": 6,
    "Salgado": 10
}
print(precos.keys())
print(type(precos.keys()))
print()

for item in precos.keys():
    print(f"O próximo item é {item}")

for preco in precos.values():
    print(f"O próximo preço é {preco}")

print("Suco" in precos.keys(), "suco" in precos.keys())
print(len(precos))

# =========================================================================

def common_elements(dict_element):
    list_element = []
    for key in dict_element.keys():
        if key in dict_element.values():
            list_element.append(key)
    return list_element

# prof cod
def common_elements(dict_element):
    return [key for key in dict_element.keys() if key in dict_element.values()]