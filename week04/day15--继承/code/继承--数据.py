"""
    继承
"""


class Person:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value


class Student(Person):
    # 构造函数
    # 1.类如果没有构造函数，解释器会自动添加一个。
    # 2.如果类有构造函数，解释器不会自动添加。
    def __init__(self,name,score):
        # 调用父类构造函数
        super().__init__(name)
        self.score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

class Teacher(Person):
    pass



stu01 = Student('zs',100)
print(stu01.name)

# teacher01 =Teacher()
#
#
# per01 = Person()
#





















