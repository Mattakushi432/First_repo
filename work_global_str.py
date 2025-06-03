"""

Для пошуку деякого символу або
підрядка у рядку можна скористатися методом find:

"""
# s = "Hi there!"
#
# start = 0
# end = 7
#
# print(s.find("er", start, end))
# print(s.find("q"))

"""

Розглянемо приклад використання translate():

"""
# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)
#
# str = "this is string example....wow!!!"
# print(str.translate(trantab))

"""

 видалення певних символів із рядка
 
"""
# intab = "aeiou"
# trantab = str.maketrans("", "", intab)
#
# str = "this is string example....wow!!!"
# print(str.translate(trantab))

"""

Програма повинна обробляти як великі, так і малі літери 
шістнадцяткових чисел і перетворювати кожен символ на його чотирибітове двійкове представлення.

"""
# symbols = "0123456789ABCDEF"
# code = [
#     '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#     '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
# ]
#
# MAP = {}
# for s, c in zip(symbols, code):
#     MAP[ord(s)] = c
#     MAP[ord(s.lower())] = c
#
# result = "34 DF 56 AC".translate(MAP)
# print(result)

"""

Наприклад, вивести числа від 0 до 7 в десятковому, шістнадцятковому, 
вісімковому і двійковому представленні можна наступним чином:

"""
# for i in range(8):
#     s = f"int: {i:d}; hex: {i:#x}; oct: {i:#o}; bin: {i:#b}"
#     print(s)

"""
Форматування за допомогою виразів у f-рядках
"""
# price = 19.99
# quantity = 3
# total = f"Total: {price * quantity:.2f}"
# print(total)

