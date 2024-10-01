# years = [1990, 1991, 2000, 2007]
# years.pop(1)
# print(years)

new_dict = {
    "Python": 1991,
    "Ruby": 1995,
    "Java": 1995,
    "Go": 2007
}

# year = new_dict.pop("Java")
# print(new_dict)
# print(year)

# year = new_dict.pop("Go")
# print(new_dict)

# # year = new_dict.pop("Rust") KeyError

# new_year = new_dict.pop("C++", 2000)
# print(new_year)

# new_year = new_dict.pop("Ruby", 2000)
# print(new_year)

del new_dict["Java"]
print(new_dict)

# del new_dict["Rust"] KeyError

def delete_keys(dict_a, list_b):
    for element in list_b:
        if element in dict_a:
            del dict_a[element]
    return dict_a