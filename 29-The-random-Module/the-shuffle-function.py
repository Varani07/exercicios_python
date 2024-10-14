import random
import copy

num = [1, 2, 3, 4]

clone = num[:]
clone = num.copy()
clone = copy.copy(num)
deep_clone = copy.deepcopy(num)

random.shuffle(clone)
print(num, clone)