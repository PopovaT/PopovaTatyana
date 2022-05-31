import re
import json
# *************************************************************
# задание1
# my_fail1 = open(r'DZ_5/ex_1.txt', 'w', encoding='utf - 8')
# line = input('Введите текст: ')
# while line:
#     line = input('Введите текст: ')
#     if not line:
#         break
# my_fail1.close()
# **************************************************************
# задание2
# my_fail2 = open(r'DZ_5/ex_2.txt', 'r', encoding='utf - 8')
# line = my_fail2.readlines()
# q_line = len(line)
# print('Строк:', q_line)
# my_fail2 = open(r'DZ_5/ex_2.txt', 'r', encoding='utf - 8')
# word = my_fail2.read()
# q_word = len(word.split())
# print('Слов:', q_word)
# my_fail2.close()
# ***************************************************************
# задание3
# my_fail3 = open(r'DZ_5/ex_3.txt', 'r', encoding='utf - 8')
# okl = my_fail3.readlines()
# ob_d = []
# min_okl = []
# for i in okl:
#     i = i.split()
#     if float(i[1]) < 20000:
#         min_okl.append(i[0])
#     ob_d.append(i[1])
#     sr_d = sum(map(float, ob_d)) / len(ob_d)
# print(min_okl)
# print(round(sr_d))
# ************************************************************************************
# задание4
# translate = {'One' : 'Один', 'Two' : "Два", 'Three' : 'Три', 'Four' : 'Четыре'}
# new_fail4 = []
# with open('DZ_5/ex_4.txt', 'r', encoding='utf - 8') as my_fail4:
#     f = my_fail4.readlines()
#     for i in f:
#         i = i.split(' ', 1)
#         new_fail4.append(translate[i[0]] + ' ' + i[1])
#     print(new_fail4, end=' ')
# with open('DZ_5/ex_4_1.txt', 'w', encoding='utf - 8') as my_fail4_1:
#     my_fail4_1.writelines(new_fail4)
# *************************************************************************************
# задание5
# my_fail5 = open(r'DZ_5/ex_5.txt', 'r+', encoding='utf - 8')
# line = input('Введите числа через пробел: ')
# my_fail5.writelines(line)
# res = line.split()
# my_sum = sum(map(float, res))
# print(my_sum)
# my_fail5.close()
# задание6
# with open(r'DZ_5/ex_6.txt', 'r', encoding='utf - 8') as my_fail6:
#     f = my_fail6.read().split('\n')
# new_fail6 = {}
# for el in f:
#     key = el.split(' ')[1:]
#     value = el.split(' ')[0]
#     new_fail6[value] = sum(map(int, re.findall(r'\d+', el)))
# print(new_fail6)
# **************************************************************************************
# задание7   НЕ ПОЛУЧАЕТСЯ(((
# def analytical_report():
#     with open(r'DZ_5/ex_7.txt', 'r', encoding='utf - 8') as my_fail7:
#         report = []
#         profit = {}
#         average_profit = {}
#         av = 0
#         prof = 0
#         i = 3
#         for line in my_fail7:
#             name, firm, earning, damage = line.split()
#             total = int(earning) - int(damage)
#             if total >= 0:
#                 prof += total
#             else:
#                 i -= 1
#                 profit[name] = total
#                 report.append((profit))
#             if i != 0:
#                 (av) = prof / i
#                 average_profit['average_profit'] = round(av)
#                 report.append(average_profit)
#             else:
#                 print('Компаний, работающих с прибылью, не найдено')
#             print(report)
#     with open(r'DZ_5/ex_7.json', 'a', encoding='utf 8') as json_f:
#         json.dump(report, json_f)
# analytical_report()
#
#
