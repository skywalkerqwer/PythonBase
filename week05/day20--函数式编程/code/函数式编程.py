class StudentModel:
    def __init__(self, id=0, name='', age=0, score=0):
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return '(%d,%s,%d,%d)' % (self.id, self.name, self.age, self.score)


def student_iter1(list_stu):
    for item in list_stu:
        if item.age >= 25:
            yield item


list_stu = [
    StudentModel(101, 'z01', 18, 100),
    StudentModel(102, 'z02', 28, 80),
    StudentModel(103, 'z03', 38, 60),
    StudentModel(104, 'z04', 48, 40),
]


# 计算所有年龄大于25的学生
def condition01(item):
    return item.age >= 25


def student_iter1(list_stu):
    for item in list_stu:
        if condition01(item):
            yield item

# 计算所有成绩大于60的学生
def condition02(item):
    return item.score >= 60


def student_iter2(list_stu):
    for item in list_stu:
        if condition02(item):
            yield item


# 计算所有成绩大于90的学生
def condition03(item):
    return item.score >= 90


def student_iter3(list_stu):
    for item in list_stu:
        if condition03(item):
            yield item


# 通用的查找方法
def student_iter(list_stu, func_condition):
    for item in list_stu:
        if func_condition(item):
            yield item

# 将函数传递到student_iter方法中
result = student_iter(list_stu,condition01)
for item in result:
    print(item)