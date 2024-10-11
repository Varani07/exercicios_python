from datetime import date

birth_day = date(2001, 9, 7)
print(birth_day)
print(type(birth_day))

moon_landing = date(year=1969, month=7, day=20)
print(moon_landing)

# date(2025, 15, 10) ValueError

print(birth_day.year)
print(birth_day.month)
print(birth_day.day)

# birth_day.year = 1999 AttributeError

today = date.today()
print(today)
print(type(today))