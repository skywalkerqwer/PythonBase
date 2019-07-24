"""
    内置高阶函数
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

"""
    查找成绩大于９０的所有学生
"""
# for item in ListHelper.find_all(list_stu,lambda i:i.score>90):
#     print(item)

# for item in filter(lambda i:i.score > 90,list_stu):
#     print(item)

"""
    获取所有学生的成绩
"""
# for item in ListHelper.select(list_stu,lambda i:i.score):
#     print(item)

# for item in map(lambda i:i.score,list_stu):
#     print(item)

"""
    排序
"""
# for item in ListHelper.order_up(list_stu,lambda i:i.score):
#     print(item)

# for item in sorted(list_stu,key= lambda i:i.score,reverse=True):
#     print(item)

"""
    最大最小值
"""
# print(ListHelper.max(list_stu,lambda i:i.age))

print(max(list_stu,key= lambda i:i.age))
