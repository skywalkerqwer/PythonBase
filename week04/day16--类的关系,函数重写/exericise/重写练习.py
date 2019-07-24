"""
    将学生管理器的StudentModel类
    用__str__ / __repr__ 重写
"""
class StudentModel:
    """
    数据模型类
    """

    def __init__(self, id=0, name='', age=0, score=0):
        """
        创建学生对象
        :param id: 编号
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

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

    def __str__(self):
        return "学号%d号,学生%s,今年%d岁,成绩%d分"%(self.id,self.name,self.age,self.score)

    def __repr__(self):
        return "StudentModel(%d,'%s',%d,%d)"%(self.id,self.name,self.age,self.score)

s01 = StudentModel(1,'张三',18,85)
print(s01)
s02 = StudentModel(2,'李四',20,90)
s03 = StudentModel(3,'王五',21,70)
s04 = eval('StudentModel(4,"赵六",22,100)')
print(s04)
list01 = [s01,s02,s03,s04]
print(list01)
s05 = eval(repr(s02))
print(s05)