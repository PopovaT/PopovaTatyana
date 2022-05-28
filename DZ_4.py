from functools import reduce
from itertools import count, cycle
from math import factorial
#задание 1
# from sys import argv
# v_ch, s_ch, pr = map(int, argv[1:])
# print((v_ch * s_ch) + pr)
# задание 2
#spisok = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#new_spisok = [print(spisok[i]) for i in range(1, len(spisok)-1) if spisok[i] > spisok[i-1]]
# Чтобы разобраться как написать в одну строку:
# for i in range(1, len(spisok)-1):
#     if spisok[i] > spisok[i-1]:
#         print(spisok[i])
##
# задание 3
# numbers = [i for i in range(20, 241) if i % 21 == 0 or i % 20 == 0]
# print(numbers)

# задание 4

# spisok1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# new_spisok = [i for i in spisok1 if spisok1.count(i) == 1]
# print(new_spisok)

# задание 5
# spisok2 =[i for i in range(100, 1001, 2)]
# res = reduce(lambda a, b: a * b, spisok2)
# print(res)

# задание 6
# a = int(input('Введите целое число: '))
# for i in count(a):
#     if i > 10:
#         break
#     else:
#         print(i)
# ***********************************************
# birthday = [0, 4, 0, 3, 1, 9, 8, 3, 10]
# res = 0
# for i in cycle(birthday):
#     if i == len(birthday) + 1:
#         break
#     else:
#         print(i)
#         i += 1
# задание 7


# def my_fact(n):
##     for i in range(n):
#         yield factorial(n)
#         break
# n = int(input('Введите число, факториал которого необходимо ввести: '))
# for el in my_fact(n):
##     print(el)
# *************************************************************************

# def my_fact2(n):
#
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#         yield fact
#
# n = int(input('Факториал чисел от 1 до: '))
# for el in my_fact2(n):
#     print(el)
