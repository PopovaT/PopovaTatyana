from abc import ABC, abstractmethod
#задание1
# class Matrix():
#     def __init__(self, list_of_lists):
#         self.lol = list_of_lists
#     def __str__(self):
#         return '\n' .join(map(str, self.lol))
#     def __add__(self, other):
#         for i in range(len(self.lol)):
#             for j in range(len(other.lol[i])):
#                 self.lol[i][j] = self.lol[i][j] + other.lol[i][j]
#         return Matrix.__str__(self)
#
# matrix1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
# matrix2 = Matrix([[3, 5, 8], [31, 43, 15], [1, 8, 12]])
# print(matrix1)
# print('_' * 30)
# print(matrix2)
# print('_' * 30)
# print(matrix1.__add__(matrix2))
#задание2
# class Clothes(ABC):
#     def __init__(self, V, H, color):
#         self.V = V
#         self.H = H
#         self.c = color
#     @property
#     def get_fabric_consumption(self):
#         return f'Общий расход ткани: {round(self.V / 6.5 + 0.5) + round(2* self.H + 0.3)} метра(ов)'
#     @abstractmethod
#     def color_clothes(self):
#         return 'Должен быть цвет'
# class Coat(Clothes):
#     def fabric_consumption(self):
#         return f'Расход ткани на пальто: {round(self.V / 6.5 + 0.5)} метра(ов).'
#     def color_clothes(self):
#         return f"Цвет: {self.c} "
# class Suit(Clothes):
#     def fabric_consumption(self):
#         return f'Расход ткани на костюм: {round(2* self.H + 0.3)} метра(ов).'
#     def color_clothes(self):
#         return f"Цвет: {self.c}"
#
# coat1 = Coat(42, 1.64, 'коричневый')
# suit1 = Suit(48, 1.79, 'чёрный')
#
# print(coat1.fabric_consumption(), coat1.color_clothes())
# print(suit1.fabric_consumption(), suit1.color_clothes())
# print(coat1.get_fabric_consumption)

#задание3
# class Cell:
#     def __init__(self, quantity):
#         self.q = int(quantity)
#     def __add__(self, other):
#         return f'Объединение двух клеток: {self.q + other.q}'
#     def __sub__(self, other):
#         subtraction = self.q - other.q
#         if subtraction > 0:
#             return f'Вычитание двух клеток: {subtraction}'
#         else:
#             return 'Результат меньше нуля'
#     def __mul__(self, other):
#         return f'Умножение двух клеток: {self.q * other.q}'
#     def __truediv__(self, other):
#         return f'Деление двух клеток: {self.q // other.q}'
#     def make_order(self, row):
#         rez = ''
#         for i in range(int(self.q / row)):
#             rez += '*' * row + '/n'
#         rez += '*' * (self.q % row)
#         return rez
# cell1 = Cell(15)
# cell2 = Cell(6)
# print(cell1 + cell2)
# print(cell1 - cell2)
# print(cell1 / cell2)
# print(cell1 * cell2)
# print(cell1.make_order(7))