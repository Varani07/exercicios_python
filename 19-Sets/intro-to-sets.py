stocks = {"MSFI", "FB", "IBM", "FB"}
print(stocks)

prices = {1, 2, 3, 4, 3, 5, 6, 7, 6, 2, 1}
print(prices)

lottery_numbers = {(1, 2, 3), (4, 4, 7), (1, 2, 3)}
print(lottery_numbers)

print(len(stocks))
print(len(prices))
print(len(lottery_numbers))

print('IBM' in stocks, "ibm" in stocks, "ibm" not in stocks)

for number in prices:
    print(number)

for numbers in lottery_numbers:
    print(numbers)
    for number in numbers:
        print(number)

nums = [-5, -4, -3, 3, 4, 5]

squares = {number ** 2 for number in nums}

print(squares, len(squares))