# задание 1
# sb = 'The Great Patriotic War'
# quest = ['Moscow', 1941, [21, 6], sb, True]
#
# for i, data in enumerate(quest, 1):
#     print(i, type(data))


# задание 2       Чуть не умерла!))))
#
# summar = list(input("Введите произвольный набор чисел: "))
#
# for i in range(0, len(summar)-1, 2):
#     summar[i], summar[i + 1] = summar[i + 1], summar[i]
# print(summar)

# задание 3
# season = {'autumn': [9, 10, 11], 'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8]}
# number_manth = int(input('Какой месяц по счету? '))
# for manth in season:
#     if number_manth in season[manth]:
#         print("It's" + " " + manth)
#         break

# задание 4
# book = input('Введите первую строчку вашего любимого стихотворения: ').split()
# for i, el in enumerate(book, 1):
#      if len(el) < 10:
#          print(i, el)
#      else:
#          print(i, (el[:10]))
# задание 5
# rtg = [ 9, 7, 4, 4, 2 ]
# el_r = int(input('Введите новый элемент рейтинга: '))
# if el_r < rtg[-1]:
#     rtg.append(el_r)
#     print(rtg)
# elif el_r > rtg[0]:
#     rtg.insert(0, el_r)
#     print(rtg)
# elif el_r in rtg:
#     rtg.insert(4, el_r)    # не знаю как записать индекс для универсальной работы программы!!!
#     print(rtg)

# задание 6  НЕ ВЫПОЛНЕНО!!!!!
# product = [
# (1, {'название': "Йодомарин", "цена": 700, "количество": 25, "ед": "уп"}),
# (2, {'название': "Анальгин", "цена": 80, "количество": 123, "ед": "уп"}),
# (3, {'название': "Дексаметазон", "цена": 3765, "количество": 8, "ед": "амп"})
# ]
# zapros = input('Выберите критерий сортировки: ').lower()

