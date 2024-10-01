metals = ["gold", "silver", "platinum", "palladium"]

print(list(filter(lambda metal: len(metal) > 5, metals)))
print(list(filter(lambda metal: "p" in metal, metals)))

print(list(map(lambda word: word.count("l"), metals)))
print(list(map(lambda word: word.replace("s", "$"), metals)))


# Meu Código
# def right_words(list_words, num):
#     new_list = []
#     for word in list_words:
#         if len(word) == num:
#             new_list.append(word)
#     return new_list

# def only_odds(list_int):
#     new_list = []
#     for numbers in list_int:
#         if numbers % 2 == 1:
#             new_list.append(numbers)
#     return new_list

# def count_of_a(list_str):
#     new_list = []
#     for strings in list_str:
#         new_list.append(strings.count("a"))
#     return new_list

# Código do Professor
# def right_words(words, num_letters):
#     return list(filter(lambda word: len(word) == num_letters, words))

# def only_odds(list_int):
#     return list(filter(lambda num: num % 2 == 1, list_int))

# def count_of_a(list_str):
#     return list(map(lambda strings: strings.count("a"), list_str))