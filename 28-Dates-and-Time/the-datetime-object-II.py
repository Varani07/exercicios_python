# from datetime import datetime

# today = datetime.today()

# print(today.strftime("%d/%m/%y"))
# print(today.strftime("%/%m/%Y"))
# print(today.strftime("%A/%m/%Y"))
# print(today.strftime("%A/%B/%Y"))

from datetime import date, time, datetime

def one_from_two(data, time_obj):
    new_date = datetime(year=data.year, month=data.month, day=data.day, hour=time_obj.hour, minute=time_obj.minute, second=time_obj.second)
    return new_date

some_date = date(2002, 2, 22)
some_time = time(9, 45, 23)
print(one_from_two(some_date, some_time))