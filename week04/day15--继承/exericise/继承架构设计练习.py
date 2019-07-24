"""
    若干个圆形(面积:半径平方×π)，若干个矩形(面积:长×宽)
    定义图形管理器：记录所有图形(圆形，矩形)的变量
                　定义计算所有图形面积总和的方法
    需求变化：可能会增加新的图形
    要求：设计架构，体现开闭原则，依赖倒置原则
"""
import math


class GraphicManager():
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        if isinstance(graphic, Shape):
            self.__graphics.append(graphic)

    def get_area(self, shape):
        if not isinstance(shape, Shape):
            return
        shape.get_area()

    def get_total_area(self):
        sum = 0
        for item in self.__graphics:
            sum += item.get_area()
        return sum


class Shape():
    """
        图形类:约束所有图形必须具有的行为
        定义所有图形的共性代码
    """

    def __init__(self, name):
        self.name = name

    def get_area(self):
        raise NotImplementedError


class Round(Shape):
    def __init__(self, name, r):
        super().__init__(name)
        self.r = r

    def get_area(self):
        return self.r ** 2 * math.pi


class Square(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


manager = GraphicManager()
c01 = Round('c01', 10)
s01 = Square('s01', 8, 5)
manager.add_graphic(c01)
manager.add_graphic(s01)
print(manager.get_total_area())
