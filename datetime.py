"""
Різниця між
    'datetime.datetime.now та datetime.now'
"""
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