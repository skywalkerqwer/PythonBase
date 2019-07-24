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

# 查找年龄大于２５的所有学生对象
# def condition01(item):
#     return item.age >= 25
# re01 = ListHelper.find_all(list_stu, condition01)

re01 = ListHelper.find_all(list_stu, lambda item: item.age >= 25)
# for item in re01:
#     print(item)

# 查找名字是z03的学生
re02 = ListHelper.frist(list_stu, lambda s: s.name == 'z03')
# print(re02)

# 成绩大于80的学生数量
re03 = ListHelper.count(list_stu, lambda c: c.score >= 80)
# print(re03)

# 查找编号是101的学生对象
re04 = ListHelper.frist(list_stu, lambda i: i.id == 101)
print(re04)

# 查找成绩小于６０的所有学生
for item in ListHelper.find_all(list_stu, lambda i: i.score < 60):
    print(item)

# 查找年龄大于２０并且成绩大于６０的所有学生
for item in ListHelper.find_all(ListHelper.find_all(list_stu, lambda i: i.age > 20), lambda j: j.score >= 60):
    print(item)

