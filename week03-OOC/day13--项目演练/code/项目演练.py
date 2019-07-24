"""
    １.定义学生类（姓名，成绩）
    2.定义根据名称查找学生对象的方法
    3.创建３个学生对象，制定不同的姓名与成绩。
    　再调用第二步的方法。
"""


class Student:
    def __init__(self, id=0, name='', score=0):
        self.name = name
        self.score = score
        self.id = id

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
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    def print_self(self):
        print(self.id, self.name, self.score)


def get_student_by_name(list_target, stu_name):
    """根据名字查找学生"""
    for item in list_target:
        if item.name == stu_name:
            return item


def get_student_by_id(list_target, stu_id):
    """根据学号查找学生"""
    for item in list_target:
        if item.id == stu_id:
            return item


def get_student_by_score(list_target, stu_score):
    """根据成绩查找学生"""
    for item in list_target:
        if item.score == stu_score:
            return item


def get_student_more_than_score(list_target, target_score):
    """查找成绩大于某数的学生"""
    list_item = []
    for item in list_target:
        if item.score >= target_score:
            list_item.append(item)
    return list_item


def get_student_by_max_score(list_target):
    """查找成绩最高的学生"""
    list_score = []
    for i in list_target:
        list_score.append(i.score)
    return get_student_by_score(list_target, max(list_score))


def get_student_by_min_id(list_target):
    """查找学号最小的学生"""
    list_id = []
    for i in list_target:
        list_id.append(i.id)
    return get_student_by_id(list_target, min(list_id))


def get_all_student_by_name(list_target, stu_name):
    """得到所有叫此名字的学生"""
    list_name = []
    for item in list_target:
        if item.name == stu_name:
            list_name.append(item)
    return list_name


def get_studen_by_down_score(list_target):
    """将学生按成绩的降序排列"""
    for i in range(len(list_target) - 1):
        for j in range(i + 1, len(list_target)):
            if list_target[i].score < list_target[j].score:
                list_target[i], list_target[j] = list_target[j], list_target[i]


def get_result(student):
    if student == None or student == []:
        print('查无此人')
    else:
        student.print_self()


list_stu = [
    Student(11, 'zs', 86),
    Student(12, 'ls', 95),
    Student(13, 'ww', 100),
    Student(14, 'zs', 85)
]
# 根据名字查找
stu = get_student_by_name(list_stu, 'zs')
get_result(stu)

# 根据学号查找
stu = get_student_by_id(list_stu, 12)
get_result(stu)

# 根据成绩查找
stu = get_student_by_score(list_stu, 100)
get_result(stu)

# 查找成绩大于９０的学生对象
stu = get_student_more_than_score(list_stu, 90)
for i in stu:
    get_result(i)

# 查找列表中成绩最高的学生
stu = get_student_by_max_score(list_stu)
get_result(stu)

# 查找列表中学号最小的
stu = get_student_by_min_id(list_stu)
get_result(stu)

# 在列表中查找指定姓名的学生(查找出全部同名学生)
list_stu_name = get_all_student_by_name(list_stu, 'zs')
for i in list_stu_name:
    get_result(i)

将学生列表按照成绩做降序排列
get_studen_by_down_score(list_stu)
for i in list_stu:
    get_result(i)
