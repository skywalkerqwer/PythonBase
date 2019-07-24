"""
    录入汽车信息(类型，速度，重量)，按e键退出，最后将每个信息显示在控制台中。
"""


class Vehicle:
    def __init__(self, type, speed, weight):
        self.type = type
        self.speed = speed
        self.weight = weight

    def print_self(self):
        print(self.type, self.speed, self.weight)


list_car = []
while True:
    car = Vehicle()
    car.type = input('type:')
    if car.type == 'e':
        break
    car.speed = input('speed:')
    if car.speed == 'e':
        break
    car.weight = input('weight:')
    if car.weight == 'e':
        break
    list_car.append(car)

for i in list_car:
    i.print_self()
