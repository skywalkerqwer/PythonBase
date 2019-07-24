"""
    练习：定义学生类（姓名，年龄）
    要求：封装数据
"""


class Student:
    def __init__(self, name='', age=0):
        self.name = name
        self.set_age(age)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value


s01 = Student('a', 1)
print(s01.name)
s01.name = 'b'
# 获取对象实例变量
print(s01.__dict__)
# dir(对象) 获取对象所有成员
print(dir(s01))

