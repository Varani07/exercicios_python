countries = ["United States", "Canada", "Australia"]
print(countries)
print(len(countries))

countries.append("Japan")
print(countries)
print(len(countries))

countries.append("France")
print(countries)
print(len(countries))

# MEU CÓDIGO
# def length_match(list_str, num):
#     count = 0
#     for strings in list_str:
#         if len(strings) == num:
#             count += 1
#     return count

# MEU CÓDIGO
# def sum_from(num1, num2):
#     total = 0
#     while num2 >= num1:
#         total += num1
#         num1 += 1
#     return total

#CÓDIGO DO PROFESSOR
# def sum_from(num1, num2):
#     total = 0
#     for number in range(num1, num2 +1):
#         total += number
#     return total

# MEU CÓDIGO
# def same_index_values(list1, list2):
#     listr = []
#     count = len(list1)
#     idx = 0
#     while count > 0:
#         if list1[idx] == list2[idx]:
#             listr.append(idx)
#         idx += 1
#         count -= 1
#     return listr  

#CÓDIGO DO PROFESSOR
# def same_index_values(list1, list2):
#     listr = []
#     for index, value in enumerate(list1):
#         if value == list2[index]:
#             listr.append(index)
#     return listr