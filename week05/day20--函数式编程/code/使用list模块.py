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

# 查找年龄大于２５的所有学生对象
from common.list_tools import ListHelper


# def condition01(item):
#     return item.age >= 25
#
#
# re01 = ListHelper.find_all(list_stu, condition01)
# for item in re01:
#     print(item)


# # 查找年龄小于３０的一个学生对象
# def condition02(item):
#     return item.age <= 30
#
#
# re02 = ListHelper.frist(list_stu, condition02)
# print(re02)

# # 查找z03学生
# def condition03(item):
#     return item.name =='z03'
# re03 = ListHelper.frist(list_stu,condition03)
# print(re03)


# 查找成绩大于80的学生数量
def condition04(item):
    return item.score >= 80
re04 = ListHelper.count(list_stu,condition04)
print(re04)