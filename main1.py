# name = input("Please enter name: ")
# other = f"Hello, {name}!"
# print(other)
from math import hypot

# a = 0.2 + 0.1  # 0.30000000000000004
# print(a)


# x = 2
# y = x != 10
# print(y)

# side_a = 10
# side_b = 5
# hypotenusa = (side_a ** 2 + side_b ** 2) ** 0.5
# print(hypotenusa)

# ratio = 10
# result = 8 * (ratio + 5) - ratio ** 2
# print(result)

# x1 = 10
# y1 = 10
# x2 = 25
# y2 = 25
# d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# print(d)

# my_list = [1, 2, 3, 4, 2, 2, 5, 2]
# count_2 = my_list.count(2)
# print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази

# my_dict = {"name": "Alice", "age": 25, "city": "New York"}  # Initialize empty dictionary
# my_dict["age"] = 26  # Змінює вік на 26
# my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
# print(my_dict)

# a = frozenset([1, 2, 3])
# b = frozenset([3, 4, 5])
#
# union = a | b  # Об'єднання множин
# intersection = a & b  # Перетин множин
# difference = a - b  # Різниця множин
# symmetric_difference = a ^ b  # Симетрична різниця
#
# print(union)  # frozenset({1, 2, 3, 4, 5})
# print(intersection)  # frozenset({3})
# print(difference)  # frozenset({1, 2})
# print(symmetric_difference)  # frozenset({1, 2, 4, 5})

# # Просте форматування рядка
# name = 'John'
# print('Hello, {}!'.format(name))
#
# # Форматування з декількома аргументами
# age = 25
# print('Hello, {}. You are {} years old.'.format(name, age))
#
# # Використання іменованих аргументів
# print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))
#
# # Використання індексів для вказівки порядку аргументів
# print('Hello, {1}. You are {0} years old.'.format(age, name))

# s = "Hello, World!"
# first_five = s[:5]
# print(first_five)  # Виведе 'Hello'

# n = 5000
# hours = n // (60 * 60)
# minutes = (n - hours * 60 * 60) // 60
# seconds = n - hours * 60 * 60 - minutes * 60

# s1 = "Hello"
# s2 = "world!"
# joined_string = s1 + " " + s2
# print(joined_string)

# # Методи списків
# my_list = [2024, 3.12]
# some_data = ['Python']
# my_list.extend(some_data)
# my_list.insert(1, 'Python')
# my_list.reverse()
# print(my_list)

# Методи словників
cat = {"nick": "Simon", "age": 7, "characteristics": "fanny"}
info = {"status": "vaccinated", "breed": True}
age = cat.get("age")
cat.update(info)
print(age)
print(cat)