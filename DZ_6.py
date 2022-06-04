import time
#задание1
# class TrafficLight():
#     count = 0
#     __color = ('red', 'yellow', 'green')
#     def running(self):
#         while TrafficLight.count < 3:
#             for el in self.__color:
#                 if el == 'red':
#                     print('Красный')
#                     time.sleep(7)
#                 elif el == 'yellow':
#                     print('Жёлтый')
#                     time.sleep(2)
#                 else:
#                     print('Зелёный')
#                     time.sleep(10)
#                     TrafficLight.count += 1
# trafficlight = TrafficLight()
# trafficlight.running()
#задание2
# class Road():
#     def __init__(self, _length, _width, massa, height):
#         self.l = _length
#         self.w = _width
#         self.m = massa
#         self.h = height
#     def kalc_asphalt(self):
#         rez = int(self.l * self.w * self.m * self.h/1000)
#         return f'Потребуется {rez} т'
# region1 = Road(20, 5000, 25, 5)
# print(region1.kalc_asphalt())
#задание3
# class Worker():
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {'wage': int(wage), 'bonus': int(bonus)}
# class Position(Worker):
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#     def get_total_income(self):
#         return self._income['wage'] + self._income['bonus']
# worker1 = Position("Иван", "Иванов", "водитель", 15000, 5000)
# print(worker1.get_full_name())
# print(worker1.get_total_income())
# worker2 = Position("Петр", "Петров", "директор", 100000, 50000)
# print(worker2.get_full_name())
# print(worker2.get_total_income())
#задание4
# class Car():
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#     def go(self):
#         return f'Машина {self.name}'
#     def stop(self):
#         return 'и остановилась.'
#     def turn(self, direction):
#         return f'повернула {direction}'
#     def sow_speed(self):
#         return f'проехала со скоростью {self.speed} км/ч,'
# class TownCar(Car):
#     def sow_speed(self):
#         if int(self.speed) > 60:
#
#             return f'превысила скорость на {int(self.speed) - 60} км/ч,'
#         else:
#             return f'проехала со скоростью {self.speed} км/ч'
# class SportCar(Car):
#     pass
# class WorkCar(Car):
#     def sow_speed(self):
#         if int(self.speed) > 40:
#             return f'превысила скорость на {int(self.speed) - 40} км/ч,'
#         else:
#             return f'проехала со скоростью {self.speed} км/ч'
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#         print('Внимание! Это полицейская машина!!!')
# car1 = TownCar('80', 'голубого цвета', 'BMV', False)
# print(car1.go(), car1.color, car1.sow_speed(), car1.turn('направо'), car1.stop())
# car2 = SportCar('120', 'жёлтого цвета', 'Chevrolet Camaro', False)
# print(car2.go(), car2.color, car2.sow_speed(), car2.turn('налево,'), car2.turn('направо'), car2.stop())
# car3 = WorkCar('39', 'зеленого цвета', 'KAMAZ', False)
# print(car3.go(), car3.color, car3.sow_speed(), car3.turn('налево,'), car3.turn('направо'), car3.stop())
# car4 = PoliceCar('110', 'сине-белого цвета', 'Toyota Camry', True)
# print(car4.go(), car4.color, car4.sow_speed(), car4.turn('налево,'), car4.turn('направо'), car4.stop())
#задание5
# class Stationery():
#     def __init__(self, title):
#         self.title = title
#     def draw(self):
#         return 'Запуск отрисовки'
# class Pen(Stationery):
#     def draw(self):
#         return f'Запуск отрисовки {self.title}'
# class Pencil(Stationery):
#     def draw(self):
#         return f'Запуск отрисовки {self.title}'
# class Handle(Stationery):
#     def draw(self):
#         return f'Запуск отрисовки {self.title}'
# pen = Pen('ручкой')
# print(pen.draw())
# pencil = Pencil('карандашом')
# print(pencil.draw())
# handle = Handle('маркером')
# print(handle.draw())