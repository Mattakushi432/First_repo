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


"""
Перетворення об'єкту datetime в timestamp і навпаки
"""
# from datetime import datetime
#
# now = datetime.now()
# timestamp = datetime.timestamp(now)
# print(timestamp)

"""
Конвертація timestamp в об'єкт datetime
"""
# from datetime import datetime
#
# timestamp = 1677721600
#
# dt_object = datetime.fromtimestamp(timestamp)
# print(dt_object)

"""
Форматування дати та часу завдяки методу strftime
"""
# from datetime import datetime
#
# now = datetime.now()
#
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_date)
#
# formatted_date_only = now.strftime("%A, %d %B %Y")
# print(formatted_date_only)
#
# formatted_date_only = now.strftime("%a, %d %B %Y")
# print(formatted_date_only)
#
# formatted_time_only = now.strftime("%I:%M %p")
# print(formatted_time_only)
#
# formatted_date_only = now.strftime("%d.%m.%Y")
# print(formatted_date_only)

"""
Перетворення раядків у об'єкти datetime за допомогою функції strptime
"""
# from datetime import datetime
#
# # Припустимо, у нас є дата у вигляді рядка
# date_string = "2023.03.14"
#
# # Перетворення рядка в об'єкт datetime
# datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
# print(datetime_object)

"""
Робота з ISO форматом дати isoformat()
"""
# from datetime import datetime
#
# now = datetime.now()
#
# iso_format = now.isoformat()
# print(iso_format)

"""
можна використати метод fromisoformat():
"""
# from datetime import datetime
#
# iso_date_string = "2025-05-12T19:28:01.859694"
#
# date_from_iso = datetime.fromisoformat(iso_date_string)
# print(date_from_iso)

"""
Метод isoweekday() у об'єкті datetime використовується для отримання дня тижня відповідно до ISO 8601.
"""
# from datetime import datetime
#
# now = datetime.now()
# day_week = now.isoweekday()
# print(f"Сьогодні: {day_week}")

"""
розглянемо корисний метод isocalendar(), який використовується для отримання кортежу
"""
# from datetime import datetime
#
# now = datetime.now()
#
# calendar = now.isocalendar()
# print(f"ISO year: {calendar[0]}, ISO week: {calendar[1]}, ISO day: {calendar[2]}")

"""
Щоб вивести дату у форматі UTC це можна зробити, 
    додавши інформацію про часову зону до об'єкта datetime:
"""
# from datetime import datetime, timezone
#
# local_now = datetime.now()
# utc_now = datetime.now(timezone.utc)
#
# print(f"Local time: {local_now}")
# print(f"UTC time: {utc_now}")

"""
Щоб перетворити час з UTC в іншу часову зону 
Східному часовому поясу США (UTC-5 годин), можна зробити наступне:
"""
# from datetime import datetime, timezone, timedelta
#
# utc_time = datetime.now(timezone.utc)
#
# eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# print(eastern_time)

"""
Щоб перетворити локальний час у час UTC спочатку потрібно призначити
локальному часу відповідну часову зону, 
а потім використати метод astimezone():
"""
# from datetime import datetime, timezone, timedelta
#
# local_timezone = timezone(timedelta(hours=2))
# local_time = datetime(year=2025, month=5, day=12, hour=20, minute=6, second=30, tzinfo=local_timezone)
#
# utc_time = local_time.astimezone(timezone.utc)
# print(utc_time)

"""
Стандарт ISO 8601 також підтримує часові зони. У Python це можна зробити, додавши інформацію про часову зону до об'єкта datetime:
"""

# from datetime import datetime, timezone, timedelta
#
# timezone_offset = timezone(timedelta(hours=2))
# timezone_datetime = datetime(year=2025, month=5, day=12, hour=20, minute=6, second=30, tzinfo=timezone_offset)
#
# iso_format_with_timezone = timezone_datetime.isoformat()
# print(iso_format_with_timezone)

"""
Метод time.time() повертає поточний час у секундах з 1 січня 1970 року (epoch time).
"""
# import time
#
# current_time = time.time()
# print(f"Текущий час: {current_time}")

"""
Метод time.sleep(seconds) зупиняє виконання програми на вказану кількість секунд
"""
# import time
#
# print("Програма зупинена")
# time.sleep(5)
# print("Програма відповідає")

"""
Метод time.ctime([seconds]) перетворює часову мітку (кількість секунд) у зрозуміле для людини текстове представлення
"""
# import time
#
# current_time = time.time()
# print(f"Поточний час: {current_time}")
#
# readable_time = time.ctime(current_time)
# print(f"Читабельний час: {readable_time}")

"""
Метод time.localtime([seconds]) перетворює часову мітку в структуру struct_time у місцевій часовій зоні.
"""
# import time
#
# current_time = time.time()
# print(f"Текущий час: {current_time}")
#
# local_time = time.localtime(current_time)
# print(f"Час в місцевій часовій зоні: {local_time}")

"""
Давайте використаємо time.perf_counter() для вимірювання часу виконання деякого блоку коду:
"""
# import time
#
# start_time = time.perf_counter()
#
# for _ in range(1_000_000):
#     pass
#
# end_time = time.perf_counter()
#
# execution_time = end_time - start_time
# print(f"Виконання блоку зі сроком {execution_time:.2f} секунд.")

