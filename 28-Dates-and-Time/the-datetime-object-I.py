from datetime import datetime

print(datetime(1999, 7, 24))
print(datetime(1999, 7, 24, 14))
print(datetime(1999, 7, 24, 14, 16, 5))
print(datetime(year=1999, month=7, day=24, hour=14, minute=16, second=5))

print()
today = datetime.today()
print(datetime.now())
print(today)
print(today.year)
print(today.hour)

print(today.weekday())

print()
same_time_future = today.replace(year=1999)
print(same_time_future)

