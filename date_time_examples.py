"""
Різниця між
    'datetime.datetime.now та datetime.now'
"""
from multiprocessing.context import set_spawning_popen

# import datetime
# now = datetime.datetime.now()
# print(now)

# from datetime import datetime
# now = datetime.now()
# print(now)

"""
    В об'єкта datetime є методи, 
        щоб отримати дату (без часу) та час (без дати):
"""
# from datetime import datetime
# current_time = datetime.now()
#
# print(current_time.date())
# print(current_time.time())

"""
Комбінування дати і часу в один об'єкт datetime
"""
# import datetime
#
# # Створення об'єктів date і time
# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12, 30, 15)
#
# # Комбінування дати і часу в один об'єкт datetime
# combined_datetime = datetime.datetime.combine(date_part, time_part)
#
# print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

"""
Для створення об'єкта datetime з певною датою:
"""
# import datetime
#
# specific_date = datetime.datetime(year=2020, month=1, day=7)
# print(specific_date)

"""
Створення об'єкта datetime з датою та часом
"""
# import datetime
#
# # Створення об'єкта datetime з конкретною датою і часом
# specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)
#
# print(specific_datetime)  # Виведе "2020-01-07 14:30:15"

"""
Використання ключових параметрів допомагає уникнути плутанини 
    та 
        забезпечує чіткість при вказівці конкретних компонентів часу. 
                    Наприклад попередній приклад можна було записати так:
"""
# from datetime import datetime
# specific_datetime = datetime(2020, 1, 7, 14, 30, 15)
#
# print(specific_datetime)

"""
Метод weekday() використовується для отримання номера дня тижня для вказаної дати. 
    Він повертає номер дня тижня, де понеділок має номер 0, а неділя - 6.
"""
# from datetime import datetime
#
# now = datetime.now()
# day_week = now.weekday()
#
# print(f"Сьогодні: {day_week}")

"""
Для порівняння двох об'єктів datetime у Python, ви можете використовувати 
стандартні оператори порівняння, такі як == (рівність), != (нерівність), < 
(менше), > (більше), <= (менше або дорівнює) та >= (більше або дорівнює). 
Ці оператори дозволяють порівнювати дати та часи, щоб визначити, чи один об'єкт 
datetime передує, наступає або є точно таким самим як інш
"""
# from datetime import datetime
#
# datetime1 = datetime(2023, 3, 14, 12, 0)
# datetime2 = datetime(2023, 3, 15, 12, 0)
#
# print(datetime1 == datetime2)
# print(datetime1 != datetime2)
# print(datetime1 < datetime2)
# print(datetime1 > datetime2)

"""
Через оператори if, elfe, else
"""
# from datetime import datetime
#
# datetime1 = datetime(2023, 3, 14, 12, 0)
# datetime2 = datetime(2023, 3, 15, 12 ,0)
#
# if datetime1 == datetime2:
#     print("NO")
# elif datetime1 <= datetime2:
#     print("YES")
# else:
#     print(None)

"""
Об'єкт timedelta можна створити, задаючи тижні, дні, години, хвилини, секунди, 
    мілісекунди і мікросекунди, передавши один або кілька з таких параметрів: 
"""
# from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta)

"""
Якщо відняти від одного datetime об'єкту інший, то отримаємо timedelta об'єкт. 
Він відповідає за відрізок часу між двома датами.
"""
# from datetime import datetime
#
# seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
#
# difference = seventh_day_2020 - seventh_day_2019
# print(difference)
# print(difference.total_seconds())

"""
Об'єкти timedelta можна створювати, щоб отримати час / дату, віддалену від початкової.
"""
# from datetime import datetime, timedelta
#
# now = datetime.now()
# future_date = now + timedelta(days=10)
# print(future_date)
"""
Або від якоїсь конкретної дати.
"""
# from datetime import datetime, timedelta
#
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# four_weeks_interval = timedelta(weeks=4)
#
# print(seventh_day_2020 + four_weeks_interval)
# print(seventh_day_2020 - four_weeks_interval)


"""
використати метод toordinal(), який повертає порядковий номер дня
"""
# from datetime import datetime
#
# date = datetime(year=2023, month=12, day=18)
# ordinal_number = date.toordinal()
# print(f"Порядковий номер {date} становить {ordinal_number}")

# from datetime import datetime
#
# napoleon_burns = datetime(year=1812, month=9, day=14)
#
# current_date = datetime.now()
#
# days_since = current_date.toordinal() - napoleon_burns.toordinal()
# print(days_since)

