cursos = {
    "História": "Denise",
    "Ciência": "Alessandra",
    "Matemática": "Cassandra"
}

for curso, prof in cursos.items():
    print(f"O curso {curso} está sendo ensinado pelo professor(a): {prof}")

for _, prof in cursos.items():
    print(f"O próximo professor é {prof}")

# ===============================================================

def sum_of_values(dict_element, list_str_element):
    soma = 0
    for string in list_str_element:
        if string in dict_element:
            for key, value in dict_element.items():
                if key == string:
                    soma += value
    return soma

def count_of_value(dict_element, int_element):
    count = 0
    for _, value in dict_element.items():
        if int_element == value:
            count += 1
    return count

def invert(dict_obj):
    new_dict = {}
    for key, value in dict_obj.items():
        new_dict[value] = key
    return new_dict

# cod. prof.
def sum_of_values(dict_element, list_str_element):
    soma = 0
    for key, value in dict_element.items():
        if key in list_str_element:
            soma += value
    return soma