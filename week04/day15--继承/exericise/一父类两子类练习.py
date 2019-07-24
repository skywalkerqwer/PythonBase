"""
    定义宠物类　数据：姓名
    定义狗类　数据：工作
    定义猫类　行为：抓
    分别创建３个类对象，调用各自成员
"""


class Pet():
    def __init__(self, name):
        self.name = name


class Dog(Pet):
    def __init__(self, name, work):
        super().__init__(name)
        self.work = work


class Cat(Pet):
    def catch(self):
        print(self.name + '抓')


dog01 = Dog('大黄', '吃')
cat01 = Cat('狗蛋')
print(dog01.name, dog01.work)
cat01.catch()
print(isinstance(dog01, Pet))
print(isinstance(dog01, Dog))
print(isinstance(cat01, Cat))
print(isinstance(cat01, Dog))
