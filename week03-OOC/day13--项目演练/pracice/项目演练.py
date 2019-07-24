"""
    在技能数据列表中查找制定名称的技能对象
    查找冷却时间大于５的所有技能对象
    查找技能数据列表中，消耗法力最小的技能
    查找技能数据列表中，冷却时间最大的技能
    根据冷却时间对进列表进行升序排列
"""


class Skill:
    __slots__ = ('__code', '__name', '__cd', '__cost_sp')

    def __init__(self, code=0, name='', cd=0, cost_sp=0, ):
        self.code = code
        self.name = name
        self.cd = cd
        self.cost_sp = cost_sp

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, value):
        self.__cd = value

    @property
    def cost_sp(self):
        return self.__cost_sp

    @cost_sp.setter
    def cost_sp(self, value):
        self.__cost_sp = value

    def print_self(self):
        print(self.code, self.name, self.cd, self.cost_sp)


list_skill = [
    Skill(1001, '两级反转', 260, 120),
    Skill(1002, '球状闪电', 0, 95),
    Skill(1003, '时间结节', 100, 300),
    Skill(1004, '混乱之祭', 165, 400)
]


def get_skill_by_name(list_target, skill_name):
    """查找指定名称的技能"""
    for item in list_target:
        if item.name == skill_name:
            return item


def get_skill_cd_more_than(list_target, skill_cd):
    """查找冷却时间大于某秒的技能"""
    list_new = []
    for item in list_target:
        if item.cd >= skill_cd:
            list_new.append(item)
    return list_new


def get_skill_by_min_cost(list_target):
    """查找消耗法力最小的技能"""
    min = list_target[0]
    for i in range(1, len(list_target)):
        if min.cost_sp > list_target[i].cost_sp:
            min = list_target[i]
    return min


def get_skill_by_max_cd(list_target):
    """查找cd时间最长的技能"""
    max = list_target[0]
    for item in range(1, len(list_target)):
        if max.cd < list_target[item].cd:
            max = list_target[item]
    return max


def get_sort_by_up_cd(list_target):
    """对冷却时间进行升序排列"""
    for i in range(len(list_target) - 1):
        for j in range(i + 1, len(list_target)):
            if list_target[i].cd > list_target[j].cd:
                list_target[i], list_target[j] = list_target[j], list_target[i]


def get_result(skill):
    if skill == None or skill == []:
        print('查无此技能')
    else:
        skill.print_self()


# 根据名称查找技能
skill = get_skill_by_name(list_skill, '球状闪电')
get_result(skill)

# 查找冷却时间大于５的所有技能
list_skill = get_skill_cd_more_than(list_skill, 5)
for i in list_skill:
    get_result(i)

# 得到消耗法力最小的技能
skill = get_skill_by_min_cost(list_skill)
get_result(skill)

# 得到冷却时间最长的技能
skill = get_skill_by_max_cd(list_skill)
get_result(skill)

# 根据冷却时间的升序进行排序
get_sort_by_up_cd(list_skill)
for i in list_skill:
    get_result(i)
