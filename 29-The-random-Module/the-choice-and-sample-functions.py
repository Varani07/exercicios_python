import random

print(random.choice(["bob", "moe", "curly"]))
print(random.choice((1, 2, 3)))
print(random.choice("Elephant"))

lottery_numbers = [random.randint(1, 50) for value in range(50)]
# print(lottery_numbers)

print(random.sample(lottery_numbers, 2))
print(random.sample(lottery_numbers, 6))