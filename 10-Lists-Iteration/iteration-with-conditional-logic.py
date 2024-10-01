# values = [3, 6, 9, 12, 15, 18, 21, 24]
# other_values = [5, 10, 15, 20, 25, 30]

# def odds_sum(numbers_list):
#     total = 0
#     for num in numbers_list:
#         if num % 2 == 1:
#             total += num
    
#     return total

# print(odds_sum(values))
# print(odds_sum(other_values))

num1 = [1, 2, 3]
num2 = [3, 2, 1]
num3 = [4, 5, 4]
num4 = [-3, -2, -1]

def greatest_number(numbers):
    g_num = numbers[0]
    for num in numbers:
        if num > g_num:
            g_num = num
    return g_num

print(greatest_number(num1))
print(greatest_number(num2))
print(greatest_number(num3))
print(greatest_number(num4))