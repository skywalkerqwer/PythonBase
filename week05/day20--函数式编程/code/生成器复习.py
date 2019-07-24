"""
    定义学生类
    分别使用生成器函数，生成器表达式，列表推导式实现
    --计算所有年龄大于25的学生
    --计算所有成绩大于60的学生
    --计算所有成绩大于90的学生
"""


class StudentModel:
    def __init__(self, id=0, name='', age=0, score=0):
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return '(%d,%s,%d,%d)'%(self.id, self.name, self.age, self.score)


def student_iter1(list_stu):
    for item in list_stu:
        if item.age >= 25:
            yield item

list_stu=[
    StudentModel(101,'z01',18,100),
    StudentModel(102,'z02',28,80),
    StudentModel(103,'z03',38,60),
    StudentModel(104,'z04',48,40),
]

# 计算所有年龄大于25的学生
re = student_iter1(list_stu)
for item in re:
    print(item)

re01 = (item for item in list_stu if item.age >= 25)
for item in re01:
    print(item)

re02 = [item for item in list_stu if item.age >= 25]
for item in re02:
    print(item)

# 计算所有成绩大于60的学生
def student_iter2(list_stu):
    for item in list_stu:
        if item.score >= 60:
            yield item

# 计算所有成绩大于90的学生
def student_iter3(list_stu):
    for item in list_stu:
        if item.score >= 90:
            yield item