"""
    需求：查找年龄最大的学生对象
    　　　查找成绩最高的学生对象
"""
class StudentModel:
    def __init__(self, id=0, name='', age=0, score=0):
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return '(%d,%s,%d,%d)' % (self.id, self.name, self.age, self.score)


list_stu = [
    StudentModel(101, 'z01', 18, 100),
    StudentModel(102, 'z02', 28, 80),
    StudentModel(103, 'z03', 38, 60),
    StudentModel(104, 'z04', 48, 40),
    StudentModel(104, 'z05', 19, 120),
]
from common.list_tools import ListHelper

re01 = ListHelper.max(list_stu,lambda i:i.age)
# print(re01)

re02 = ListHelper.max(list_stu,lambda i:i.score)
# print(re02)

"""
    需求：
    累加所有学生的成绩
"""
re03 = ListHelper.sum(list_stu,lambda i:i.score)
# print(re03)

"""
    需求：
    获取所有学生的姓名
"""
re04 = ListHelper.select(list_stu,lambda i:i.name)
# for item in re04:
#     print(item)

"""
    需求：
    按照成绩对学生列表进行升序排列
"""
ListHelper.order_up(list_stu,lambda i:i.score)
for item in list_stu:
    print(item)