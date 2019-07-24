"""
    继承
"""


class Person:
    def say(self):
        print('说话')


class Student(Person):
    def study(self):
        print('学习')


class Teacher(Person):
    def teach(self):
        print('教学')

stu01 = Student()
stu01.study()
stu01.say()

teacher01 =Teacher()
teacher01.say()

per01 = Person()
per01.say()

# 判断对象是否兼容类
print(isinstance(stu01,Student))
print(isinstance(stu01,Teacher))
print(isinstance(stu01,Person))

























