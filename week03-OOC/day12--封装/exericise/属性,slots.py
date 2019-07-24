"""
    练习 Student类 (姓名，年龄，成绩，性别)
"""


class Student:
    __slots__ = ('__name', '__age', '__score', '__sex') #限定对象只能有这些实例变量

    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value):
        self.__sex = value


s01 = Student(1, 2, 3, 4)
print(s01.name)
