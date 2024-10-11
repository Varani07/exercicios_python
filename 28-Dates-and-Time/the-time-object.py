from datetime import time

start = time()
print(start, type(start), start.hour, start.minute, start.second)

print(time(6))
print(time(hour=6))
print(time(hour=18))

print(time(12, 25))
print(time(hour=12, minute=25))

print(time(23, 32, 22))
evening = time(hour=23, minute=32, second=22)
print(evening.hour)
print(evening.minute)
print(evening.second)

# time(27) ValueError