
# задание 1

# subject = input("Введите название предмета: ") # предмет
# eval = str(input("Введите оценки: "))  # оценки
# result = subject + " " + eval # результат
# print("Результат: " + (result))



# dist = int(input("Введите дистанцию (в метрах): "))
# name1 = input("Введите имя первого спортсмена: ")
# time = float(input("Введите время первого спортсмена: "))
# res1 = round(dist/time)
# print(str(res1) + "м/мин")
# name2 = input("Введите имя второго спортсмена: ")
# time = float(input("Введите время второго спортсмена: "))
# res2 = round(dist/time)
# print(str(res2) + "м/мин")
# name3 = input("Введите имя третьего спортсмена: ")
# time = float(input("Введите время третьего спортсмена: "))
# res3 = round(dist/time)
# print(str(res3) + "м/мин")
# finres = float(max(res1, res2, res3))
# print("Лучшая скорость: " + str(finres))
# if finres == res1:
#     print("Победитель: " + name1)
# elif finres == res2:
#     print("Победитель: " + name2)
# else:
#     print("Победитель: " + name3)
# print("Поздравляем!!!")

# задание 2
# time = int(input("Введите время в секундах: "))
#
# h = time//3600
# m = (time - (h * 3600)) // 60
# s = time - ((m * 60) + (h * 3600))
# print(h, ":", m, ":", s)
# задание 3
# n = int(input("Введите n: "))
# a = n
# b = n*11
# c = n*111
# result = a + b + c
# print(result)

# задание 4
# numbers = int(input("Введите целое число: "))
# max = numbers % 10
# numbers = numbers // 10
# while  numbers > 0:
#     if numbers > max:
#         max = numbers % 10
#         numbers = numbers // 10
# print(max)


# numbers = input("Введите целое число: ")
# print(max(numbers))

# задание 5
# +
# задание 6
# vr = int(input("Введите сумму выручки: "))
# izd = int(input("Ввведите сумму издержек: "))
# if vr > izd:
#     r = round(((vr - izd)/vr) * 100)
#     print('Рентабельность: ' + str(r), "%" + ', Вы в плюсе!')
#
# else:
#     print("Проведите анализ работы своей фирмы!")
# p = int(input("Введите численность сотрудников вашей фирмы: "))
# pr = round(int(vr-izd)/p)
# print("Прибыль на одного сотрудника: "  + str(pr) + " рублей")

# задание 7
# a = int(input("Введите текущий результат: "))
# b = int(input("Введите желаемый результат: "))
# day = 1
#
# while a < b:
#     print(str(day) + "-й" + " день" + "-", a)
#     a += round(a * 0.1)
#     day += 1
# print("На " + str(day) + " день Вы достигните желаемого результата")










