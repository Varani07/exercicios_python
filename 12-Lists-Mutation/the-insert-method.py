plays = ["Hamlet", "Macbeth", "King Lear"]

plays.insert(1, "Julius Caesar")
print(plays)

plays.insert(0, "Romeo & Juliet")
print(plays)

plays.insert(10, "A Midsummer Night's Dream")
print(plays)


# MEU CÓDIGO

# def factors(number):
#     list_num = []
#     for num in range(number, 0, -1):
#         list_num.insert(0, number)
#         number = number//2
#         if number == 0:
#             break
#     return list_num

# CÓDIGO DO PROFESSOR

# def factors(number):
#     my_factors = []

#     for i in range(1, number + 1):
#         if number % i == 0:
#             my_factors.append(i)
#     return my_factors