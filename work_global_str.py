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

n = int(input())
i = [0, 1, 2]
for _ in range(n):
    print(i)
    i = [i[1], i[2], i[0] + i[1] + i[2]]