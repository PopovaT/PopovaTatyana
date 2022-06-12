# задание 1
# class Data:
#     def __init__(self, day_month_year):
#         self.day_month_year = day_month_year
#     @classmethod
#     def convert(cls, day_month_year):
#         new_data = []
#         for i in day_month_year.split('-'):
#             if i != '-':
#                 new_data.append(i)
#         return int(new_data[0]), int(new_data[1]), int(new_data[2])
#
#     @staticmethod
#     def valid(day, month, year):
#         if day > 1 and day < 31:
#             if month > 1 and month < 12:
#                 if year > 0 and year < 2022:
#                     return 'OK'
#                 else:
#                     return f'Неверно введен год'
#             else:
#                 return f'Неверно введен месяц'
#         else:
#             return f'Неверная дата'
#     def __str__(self):
#         return f'Сегодня: {Data.convert(self.day_month_year)}'
#
# day1 = Data('15-10-2020')
# print(day1)
# print(Data.valid(12, 10, 2025))
# print(day1.convert('30-11-2012'))
#
# # задание 2
# class DivNullError:
#     def __init__(self, delim, delit):
#         self.delim = delim
#         self.delit = delit
#     @staticmethod
#     def dev_null_error(delim, delit):
#         try:
#             return delim/delit
#         except:
#             return (f'Деление на ноль')
# div1 = DivNullError(50, 10)
# print(DivNullError.dev_null_error(35, 0))
# print(div1.dev_null_error(77, 2))
# print(div1.dev_null_error(2, 0))

# задание 3
# class OnlyInt:
#     def __init__(self, *args):
#         self.lst = []
#     def input1(self):
#         while True:
#             try:
#                 v = int(input('Введите значение: '))
#                 self.lst.append(v)
#                 print(f'Вы ввели: {self.lst} \n')
#             except:
#                 print('Только числа')
#                 v1 = input(f'Продолжить? +/-')
#                 if v1 == '+':
#                     return error.input1()
#                 elif v1 == '-':
#                     return 'Goodbay'
# error = OnlyInt(3)
# print(error.input1())
# задание 7
# class ComplexNum:
#     def __init__(self, a, b, *args):
#         self.a = a
#         self.b = b
#         self.r = 'a + bj'
#     def __add__(self, other):
#         return f'Сумма: {self.a + other.a} + {self.b + other.b}j'
#     def __mul__(self, other):
#         return f'Произведение: {self.a * other.a - (self.b * other.b)} + {self.b * other.b}j'
#     def __str__(self):
#         return f'{self.a} + {self.b}j'
#
# r1 = ComplexNum(3, 7)
# r2 = ComplexNum(4, 1)
# print(f'Первое число: {r1}')
# print(f'Второе число: {r2}')
# print(r1 + r2)
# print(r1 * r2)
# задание 4, 5, 6
# class Tehnik:
#     def __init__(self, name, price, quantity, num_in_list, *args):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.num = num_in_list
#         self.my_st_full = []
#         self.my_st = []
#         self.unit = {'Модель': self.name, 'Цена': self.price, 'Количество': self.quantity}
#     def __str__(self):
#         return f'{self.name} цена {self.price} количество {self.quantity}'
#     def reception(self):
#         try:
#             unit = input(f'Введите наименование: ')
#             unit_p = int(input(f'Введите стоимость (едю): '))
#             unit_q = int(input(f'Введите количество: '))
#             unique = {'Модель устройства': unit, 'цена': unit_p, "Количество": unit_q}
#             self.unit.update(unique)
#             self.my_st.append(self.unit)
#             print(f'Список: \n {self.my_st}')
#         except:
#             return f'Проверьте введенные данные'
#         print(f'Выход - Q')
#         q = input().lower()
#         if q:
#             self.my_st_full.append(self.my_st)
#             print(f'Весь товар -\n {self.my_st_full}')
#             return 'Выход'
#         else:
#             return Tehnik.reception(self)
# class Printer(Tehnik):
#     def prints(self):
#         return f'Что-то печатает {self.num}'
#
# class Scanner(Tehnik):
#     def scans(self):
#         return f'Что-то сканирует {self.num}'
# class Copier(Tehnik):
#     def copies(self):
#         return f'Что-то копирует {self.num}'
#
#
# product1 = Printer('Canon', 3500, 7, 15)
# product2 = Scanner('HP', 1500, 7, 15)
# product3 = Copier('Canon', 1200, 1, 10)
# print(product1.reception())
# print(product2.reception())
# print(product3.reception())
# print(product1.prints())
# print(product3.copies())



