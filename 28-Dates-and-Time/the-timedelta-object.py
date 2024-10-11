from datetime import timedelta, datetime

birth_day = datetime(2001, 9, 7)
today = datetime.now()

my_life_span = today - birth_day

print(my_life_span)
print(type(my_life_span))
print(my_life_span.total_seconds())

five_hundred_days = timedelta(days=500, hours=12)
print(five_hundred_days)
print(five_hundred_days + five_hundred_days)
print(today + five_hundred_days)
print(today - my_life_span)