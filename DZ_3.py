# задание 1
#
# def schet(num1, num2):
#     try:
#         return num1/num2
#
#     except ZeroDivisionError:
#         return ("Вы пытаетесь делить на ноль!!!")
#
# n1 = int(input("Введите первое число: "))
# n2 = int(input("Введите второе число: "))
#
# print(schet(n1, n2))
# **************************************************************************
# задание 2
# def anketa(surname,name, age, live_town, email, tel_number):
#     return print(surname, name, (2022 - age), live_town, email, tel_number)
# anketa(
# surname=input("Фамилия: ").title(),
# name=input("Имя: ").title(),
# age=int(input("Год рождения: ")),
# live_town=input("Город проживания: ").title(),
# email=input("Ваш email: "),
# tel_number=int(input("Номер телефона: "))
# )
# ***************************************************************************
# задание 3
# def my_func(num1, num2, num3):
#     return (num1 + num2), (num2 + num3), (num1 + num3)
# res = my_func(
# num1=int(input("Первое число: ")),
# num2=int(input("Второе число: ")),
# num3=int(input("Третье число: "))
# )
# print(max(res))
# ***************************************************************************
# задание 4
# первый способ
# def  my_func(x,y):
#     return print(x**y)
# my_func(
# x = int(input("X: ")),
# y = int(input("Y: "))
# )
# второй способ
# def my_func(x,y):
#     res = x
#     for sq in range(abs(y-1)):
#         res /= x
#     return print(res)
# my_func(
# x = int(input("X: ")),
# y = int(input("Y: "))
# )
# ***************************************************************************
# задание 5
# def new_func():
#     res = 0
#     try:
#         while True:
#             chi = input('Введите числа или "*" для выхода ').split()
#             for i in chi:
#                 if i == '*':
#                     print(res)
#                     return
#                 else:
#                     res += float(i)
#             print(res)
#     except ValueError:
#         print(res)
#         print('Goodbay')


new_func()

# задание 6 + 7
# def int_func():
#     a = input("Text: ").title()
#     return print(a)
#
# int_func()