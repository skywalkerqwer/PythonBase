"""
    录入学生信息：姓名，成绩，性别，年龄
    步骤1：创建类，定义4个数据成员
    步骤2：在控制台中循环3次输入学生成绩
"""


class StudentInfo:
    count = 0

    def __init__(self, name='', score=0, sex='', age=0):
        self.name = name
        self.score = score
        self.sex = sex
        self.age = age

    def print_self(self):
        print(self.name,self.score,self.sex,self.age)


list_stu = []
for i in range(4):
    stu = StudentInfo()
    stu.name = input('name:')
    stu.score = input('score:')
    stu.sex = input('sex:')
    stu.age = input('age')
    list_stu.append(stu)

for i in list_stu:
    i.print_self()