# # # if __name__ == '__main__':
# # #     a = int(input("enter first number: "))
# # #     b = int(input("enter second number: "))
# # #     total = a + b
# # #     differece = a - b
# # #     product = a * b
# # #     # Процентная
# # #     # разница = | (a - b) / [(a + b) / 2] |
# # #     # *100 %
# # from typing import List
# #
# # from PIL.EpsImagePlugin import has_ghostscript
# #
# # # def square_sum(numbers):
# # #     return sum(x*x for x in numbers)
# # #
# # # assert (square_sum([1,2]) == 5)
# # # # assert (square_sum([0, 3, 4, 5]) == 50)
# # # # assert (square_sum([]) == 0)
# # # # assert (square_sum([-1,-2]) == 5)
# # # # assert (square_sum([-1,0,1]) == 2)
# # # print(square_sum([1,2]))
# #
# #
# # # def paperwork(n, m):
# # #     if n < 0 or m < 0:
# # #         return 0
# # #     return n * m
# # #
# # # assert (paperwork(5,5) == 25), "Failed at Paperwork(5,5)"
# # # test.assert_equals(paperwork(1,2), 2, "Failed at Paperwork(1,2)")
# # # test.assert_equals(paperwork(-5,5), 0, "Failed at Paperwork(-5,5)")
# # # test.assert_equals(paperwork(5,-5), 0, "Failed at Paperwork(5,-5)")
# # # test.assert_equals(paperwork(-5,-5), 0, "Failed at Paperwork(-5,-5)")
# # # test.assert_equals(paperwork(5,0), 0, "Failed at Paperwork(5,0)")
# #
# # # is_next = None
# # # num = int(input("Enter the number of points: "))
# # # if num >= 83:
# # #     is_next = True
# # # else:
# # #     is_next = False
# #
# # work_experience = int(input("Enter your full work experience in years: "))
# # if 2 <= work_experience <= 5:
# #     developer_type = "Middle"
# # elif work_experience <= 1:
# #     developer_type = "Junior"
# # else:
# #     developer_type = "Senior"
# # print(developer_type)
#
#
# # work_experience = int(input("Enter your full work experience in years: "))
# # if 1 <= 5:
# #     developer_type = ("Middle")
# # elif 1 > 0:
# #     developer_type = ("Beginner")
# # else:
# #     developer_type = ("Expert")
# #
# #
# #
# # # def minimum(arr):
# # #     return min(arr)
# # #
# # # assert minimum([-52, 56, 30, 29, -54, 0, -110]) == -110
# # # assert minimum([42, 54, 65, 87, 0]) == 0
# # # assert minimum([1, 2, 3, 4, 5, 10]) == 1
# # # assert minimum([-1, -2, -3, -4, -5, -10]) == -10
# # # assert minimum([9]) == 9
# # #
# # #
# # # def maximum(arr):
# # #     return max(arr)
# # #
# # # assert maximum([-52, 56, 30, 29, -54, 0, -110]) == 56
# # # assert maximum([4, 6, 2, 1, 9, 63, -134, 566]) == 566
# # # assert maximum([5]) == 5
# # # assert maximum([534, 43, 2, 1, 3, 4, 5, 5, 443, 443, 555, 555]) == 555
# # # assert maximum([9]) == 9
# #
# #
# # # a = 15
# # # b = 10
# # # if a > b: # a > b Умова
# # #     print()
# #
# # # a = input('Введіть число')
# # # a = int(a)
# # #
# # # if a > 0:
# # #     print('Число додатне')
# # # elif a == 1:
# # #     print('Число дорівнює 1')
# # # else:
# # #     print("a <= 0")
# #
# #
# # # num = 15 # приклад значення для num
# # #
# # # if num > 10:
# # #     print("num більше за 10")
# # # else:
# # #     print("num не більше за 10")
# #
# # # money = 0
# # # if money:
# # #     print(f"You have {money} on your bank account")
# # # else:
# # #     print("You have no money and no debts")
# #
# # # result = None
# # # if result:
# # #     print(result)
# # # else:
# # #     print("Result is None, do something")
# #
# # # name = "Taras"
# # # age = 22
# # # has_driver_licence = True
# # #
# # # if name and age >= 18 and has_driver_licence:
# # #     print(f"User {name} can rent a car")
# #
# # # # Задаємо конкретне число
# # # num = int(input())
# # #
# # Запитуємо ціле число від користувача
# num = int(input("Введіть ціле число: "))
# result = ""  # Ініціалізуємо змінну
#
# if num > 0:
#     if num % 2 == 1:
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"
#
# print(result)
#
# # # # Перевіряємо кратність
# # # if num % 3 == 0 and num % 5 == 0:
# # #     print("FizzBuzz")
# # # elif num % 3 == 0:
# # #     print("Fizz")
# # # elif num % 5 == 0:
# # #     print("Buzz")
# # # else:
# # #     print(num)
# #
# # # if x >= 0:
# # #     if y >= 0:  # x > 0, y > 0
# # #         print("Перша чверть")
# # #     else:  # x > 0, y < 0
# # #         print("Четверта чверть")
# # # else:
# # #     if y >= 0:  # x < 0, y > 0
# # #         print("Друга чверть")
# # #     else:  # x < 0, y < 0
# # #         print("Третя чверть")
# #
# #
# # # is_nice = True
# # # state = "nice" if is_nice else "not nice"
# #
# # # fruit = "cherry"
# # #
# # # match fruit:
# # #     case "apple":
# # #         print("This is an apple.")
# # #     case "banana":
# # #         print("This is a banana.")
# # #     case "orange":
# # #         print("This is an orange.")
# # #     case "cherry":
# # #         print("This is a cherry.")
# # #     case _:
# # #         print("Unknown fruit.")
# #
# # # point = (1, 0)
# # #
# # # match point:
# # #     case (0, 0):
# # #         print("Точка в центрі координат")
# # #     case (0, y):
# # #         print(f"Точка лежить на осі Y: y={y}")
# # #     case (x, 0):
# # #         print(f"Точка лежить на осі X: x={x}")
# # #     case (x, y):
# # #         print(f"Точка має координати:  x={x}, y={y}")
# # #     case _:
# # #         print("Це не точка")
# #
# #
# # # pets = ["dog", "fish", "cat"]
# # #
# # # match pets:
# # #     case ["dog", "cat", _]:
# # #         # Випадок, коли є і собака, і кіт
# # #         print("There's a dog and a cat.")
# # #     case ["dog", _, _]:
# # #         # Випадок, коли є тільки собака
# # #         print("There's a dog.")
# # #     case _:
# # #         # Випадок для інших комбінацій
# # #         print("No dogs.")
# #
# #
# # # fruit = 'apple'
# # # for char in fruit:
# # #     print(char)
# #
# #
# # # car = "Volvo", "BMW", "Audi"
# # # for brand in car:
# # #     print(brand)
# #
# # # alphabet = "abcdefghijklmnopqrstuvwxyz"
# # # for char in alphabet:
# # #     print(char, end=" ")
# #
# # # some_iterable = ["a", "b", "c"]
# # #
# # # for i in some_iterable:
# # #     print(i)
# #
# # # odd_numbers = [1, 3, 5, 7, 9]
# # # for i in odd_numbers:
# # #     print(i ** 2)
# #
# # # # Зчитування рядка від користувача
# # # user_input = input("Введіть рядок: ")
# # #
# # # # Ініціалізація змінних для підрахунку символів та пробілів
# # # total_chars = len(user_input)  # загальна кількість символів у рядку
# # # space_count = 0  # кількість пробілів
# # #
# # # # Підрахунок кількості пробілів
# # # for char in user_input:
# # #     if char == " ":
# # #         space_count += 1
# # #
# # # # Виведення результатів
# # # print(f"Загальна кількість символів у рядку: {total_chars}")
# # # print(f"Кількість пробілів у рядку: {space_count}")
# #
# # # k = 0
# # # while k < 10:
# # #     k = k + 1
# # #     print(k)
# #
# # # num = 0
# # # while num < 10:
# # #     num = num + 1
# # #     if num % 2 == 0:
# # #         continue
# # #     print(num)
# #
# # # a = 0
# # # while True:
# # #     print(a)
# # #     if a >= 5:
# # #         break
# # #     a = a + 1
# #
# # # a = 0
# # # while a < 6:
# # #     a = a + 1
# # #     if not a % 2:
# # #         continue
# # #     print(a)

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# while num > 0:
#     sum = sum + num
#     num = sum - num
#     print(sum)
# # (n * (n + 1 )) / 2
#
# start = 0
# end = 100
# a = start
# s = 0
#
# while a < end+1:
#     if a == end:
#         print(end, end='\n')
#     else:
#         print(a, end='+')
#
#     s += a
#     a = a + 1
#
# print("Сумма:", s)
#
#
#
#

# k = 0
# while k < 10:
#     k = k + 1
#     print(k)


# #
# # # for i in range(1, 10):
# # #     if i % 2 == 0:
# # #         print(f"{i} є парним числом.")
# # #     else:
# # #         print(f"{i} є непарним числом.")
# #
# #
# # # for i in range(5):
# # #     print(i)
# #
# # # for i in range(2, 10):
# # #     print(i)
# #
# # # for i in range(0, 10, 2):
# # #     print(i)
# #
# #
# # # some_list = ["apple", "banana", "cherry"]
# # # for index, value in enumerate(some_list):
# # #     print(index, value)
# #
# # # list1 = ["зелене", "стигла", "червоний"]
# # # list2 = ["яблуко", "вишня", "томат"]
# # # for number, letter in zip(list1, list2):
# # #     print(number, letter)
# #
# # # list1 = [1, 2, 3]
# # # list2 = ['a', 'b', 'c', 'd', 'e']
# # #
# # # for number, letter in zip(list1, list2):
# # #     print(number, letter)
# #
# # # numbers = {
# # #     1: "one",
# # #     2: "two",
# # #     3: "three"
# # # }
# # #
# # # for key in numbers:
# # #     print(key)
# #
# # # def say_hello():
# # #     print("Hello!")
# #
# # # def print_max(a, b):
# # #     if a > b:
# # #         print(a, 'максимально')
# # #     elif a == b:
# # #         print(a, 'дорівнює', b)
# # #     else:
# # #         print(b, 'максимально')
# # #
# # # print_max(3, 4)  # пряма передача значень
# # #
# # # x = 5
# # # y = 7
# # # print_max(x, y)  # передача змінних як аргументів
# #
# #
# # # def print_max(a: int, b: int):
# # #     if a > b:
# # #         print(a, 'максимально')
# # #     elif a == b:
# # #         print(a, 'дорівнює', b)
# # #     else:
# # #         print(b, 'максимально')
# # #
# # # print_max(3, 4)  # пряма передача значень
# # #
# # # x = 5
# # # y = 7
# # # print_max(x, y)  # передача змінних як аргументів
# #
# # # def my_function() -> ReturnType:
# # #     return result
# #
# # ## Виведення числа
# # # def add_numbers(num1: int, num2: int) -> int:
# # #     sum = num1 + num2
# # #     return sum
# # # result = add_numbers(5, 10)
# # # print(result)
# #
# # ## Виведення строки
# # # def greet(name: str) -> str:
# # #     return f"Hello {name}!"
# # # greeting = greet("John")
# # # print(greeting)
# #
# # ## Функція, що повертає булеве значення:
# # # def  is_even(num: int) -> bool:
# # #     return num % 2 == 0
# # # check_even = is_even(4)
# # # print(check_even)
# #
# # ## Принципи змінності об'єктів у Python
# # # def modify_string(original: str) -> str:
# # #     original = "changed"
# # #     return original
# # # str_var = "original"
# # # print(modify_string(str_var))
# # # print(str_var)
# #
# # ## Змінні типи, як списки list
# # # def modify_list(lst: list) -> None:
# # #     lst.append(4)
# # #
# # # my_lsit = [1, 2, 3]
# # # modify_list(my_lsit)
# # # print(my_lsit)
# #
# # ## Використовуйте метод copy() для створення копій змінних об'єктів, якщо не хочете змінювати оригінал.
# # ## Тут список my_list після виконання функції modify_list вже не зазнає змін.
# # # def modify_list(lst: list) -> None:
# # #     lst = lst.copy()
# # #     lst.append(4)
# # #
# # # my_lsit = [1, 2, 3]
# # # modify_list(my_lsit)
# # # print(my_lsit)
# #
# # ## конвертувати кожен символ у рядку в його відповідний код ASCII.
# # # def string_to_ascii(string: str) -> dict:
# # #     ascii_dict = {"A": 65, "B": 66, "C": 67}
# # #     for char in string:
# # #         if char not in ascii_dict:
# # #             ascii_dict[char] = ord(char)
# # #     return ascii_dict
# #
# # ## Після виклику функції string_to_codes із рядком "Hello world!"
# # # def string_to_codes(string: str) -> dict:
# # #     result = string_to_codes("Hello world!")
# # #     return result
# #
# #
# # ## змінна, оголошена всередині функції
# # # x = 50
# # # def func() -> None:
# # #     x = 2
# # #     print('var local x on', x)
# # #
# # # func()
# # # print('Global x and earlier', x)
# #
# # ## функція визначена всередині іншої функції
# # # def outer_func():
# # #     enclosing_var = "Я змінна в функції, що охоплює"
# # #
# # #     def inner_func():
# # #         print("Всередині вкладеної функції:", enclosing_var)
# # #
# # #     inner_func()
# # # outer_func()
# #
# # ## Для того, щоб розібратися як змінювати змінні в функції, що охоплює внутрішню функцію, розглянемо приклад:
# # # def func_outher():
# # #     x = 2
# # #
# # #     def func_inner():
# # #         nonlocal x
# # #         x = 5
# # #
# # #     func_inner()
# # #     return x
# # # result = func_outher()
# #
# # ## щоб змінити глобальну змінну всередині функції, необхідно використовувати ключове слово global.
# # # x = 50
# # #
# # # def func():
# # #     global x
# # #     print('numbers дорівнює', x)
# # #     x = 2
# # #     print('Змінюємо глобальне значення numbers на')
# # #
# # # func()
# # # print('Значення numbers складає', x)
# #
# # ## Визначимо функцію з ключовими аргументами
# # # def greet(name, message="Hello"):
# # #     print(f"{message}, {name}!")
# #
# # ## приклад для демонстрації гнучкості ключових аргументів, та можливості змінювати порядок аргументів або використовувати значення за замовчуванням.
# # # def func(a, b=5, c=10):
# # #     print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)
# # # func(3, 7)
# # # func(25, c = 24)
# # # func(c = 50, a = 100)
# #
# # ## виведення на екран рядка, вказаного число разів.
# # # def say(message, time=1):
# # #     print(message * time)
# # # say("Hello")
# # # say("World", 5)
# #
# # ## Нам необхідно створити функцію для розрахунку вартості товарів з урахуванням можливої знижки.
# # # def real_cost(base: int, discount: float = 0) -> float:
# # #     return base * (1 - discount)
# # # price_bread = 15
# # # price_butter = 50
# # # price_sugar = 60
# # #
# # # current_price_bread = real_cost(price_bread)
# # # current_price_butter = real_cost(price_butter, 0.05)
# # # current_price_sugar = real_cost(price_sugar, 0.07)
# # #
# # # print(f"new price: {current_price_bread}")
# # # print(f"new price: {current_price_butter}")
# # # print(f"new price: {current_price_sugar}")
# #
# # ## робота з винятками
# # # while True:
# # #     age = input("How old are you? ")
# # #     try:
# # #         age = int(age)
# # #         if age >= 18:
# # #             print("Access allowed!")
# # #             break
# # #         else:
# # #             print("Access denied!")
# # #             break
# # #     except ValueError:
# # #         print(f"{age} is not a number, please write a number!")
# # #     finally:
# # #         print("_" * 100)
# #
# # ## Приклад використання параметру *args
# # # def printy_all_args(*args):
# # #     for arg in args:
# # #         print(arg)
# # # printy_all_args(1, "Hello", True)
# #
# # # def concatenate(*args):
# # #     result = ""
# # #     for arg in args:
# # #         result += arg
# # #     return result
# # #
# # # print(concatenate("Hello", " ", "world", "!"))
# #
# # # def concatenate(*strings):
# # #     result = ""
# # #     for string in strings:
# # #         result += string
# # #     return result
# # # print(concatenate("Hello", " ", "world", "!"))
# #
# # ## Приклад використання параметру **kwargs
# # # def greet(**kwargs):
# # #     for key, value in kwargs.items():
# # #         print(f"{key}: {value}")
# # # greet(name="Alice", age=25)
# #
# # # def example_function(*args, **kwargs):
# # #     print("Позиційні аргументи:", args)
# # #     print("Ключові аргументи:", kwargs)
# # # example_function(1, 2, 3, name="Alice", age=25)
# #
# # ## Розпакування списку дозволяє присвоїти елементи списку окремим змінним.
# # # my_list = [1, 2, 3]
# # # a, b, c = my_list
# # # print(a, b, c)
# #
# # # def greet(name, age):
# # #     print(f"Hello {name}, you are {age} years old.")
# # #
# # # person_info = {"name": "Alice", "age": 25}
# # # greet(**person_info)
# #
# # ## Запоковка списку
# # # a = 1
# # # b = 2
# # # c = 3
# # # packed = [a, b, c]
# # # print(packed)
# #
# # ## Формула обчислення факторіала
# # # def factorial(n):
# # #     if n == 0:
# # #         return 1
# # #     else:
# # #         return n * factorial(n - 1)
# # # print(factorial(5))
# #
# # ## Формула обчислення фібоначчі
# # # def fibonacci(n):
# # #     if n == 0:
# # #         return 0
# # #     elif n == 1:
# # #         return 1
# # #     else:
# # #         return fibonacci(n - 1) + fibonacci(n - 2)
# # # print(fibonacci(10))
# #
# # # def fibonacci(n):
# # #     if n <= 1:
# # #         return  n
# # #     else:
# # #         return fibonacci(n - 1) + fibonacci(n - 2)
# # # print(fibonacci(10))
# #
# # ## як працює стек викликів у рекурсії на прикладі функції для обчислення факторіала числа:
# # # def factorial(n):
# # #     print("Виклик функції factorial з n = ", n)
# # #     if n == 1:
# # #         print("Базовий віпадок, n = 1, повернення 1")
# # #         return 1
# # #     else:
# # #         result = n * factorial( n - 1)
# # #         print("Повернення результату для n = ", n, ": ", result)
# # #         return result
# # # print(factorial(5))


# # Запитуємо у користувача число від 0 до 100
# num = int(input("Введіть ціле число від 0 до 100: "))
# sum = 0
# if 0 <= num <= 100:
#     sum = 0
#
#     while num >= 1:
#         sum += num
#         num -= 1
#
#     print("Сума всіх чисел від 1 до введеного числа дорівнює:", sum)
# else:
#     print("Число повинно бути від 0 до 100.")


# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for char in message:
#     if char == "r":
#         result += 1
# print(result)


# pool = 1000
# quantity = int(input("Enter the nuymber of mailings: "))
#
# try:
#     chunk = pool // quantity
#     print(f"Each mailing will cost {chunk} dollars.")
# except ZeroDivisionError:
#     print("You can't send mailings without quantity.")


# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price
#         price = price * (1 - discount)
#
#     apply_discount()
#     return price


# def get_fullname(first_name, last_name, middle_name=""):
#     if middle_name:
#         return f"{first_name} {middle_name} {last_name}"
#     else:
#         return f"{first_name} {last_name}"

# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     padding = " " * ((length - len(string)) // 2)
#     return padding + string



# def first(size, *args):
#     for arg in args:
#         print(f"{arg}: {size}")
#     return len(args)  # Return something meaningful
#
# def second(size, **kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {size} -> {value}")
#     return len(kwargs)  # Return something meaningful
#
# print(first(5, "first", "second", "third"))
# print(first(1, "Alex", "Boris"))
# print(second(3, comment_one="first", comment_two="second", comment_third="third"))
# print(second(10, comment_one="Alex", comment_two="Boris"))
