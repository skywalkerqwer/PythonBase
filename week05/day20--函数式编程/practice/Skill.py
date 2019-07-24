"""
    技能(编号,名称,法力消耗,冷却时间)
    实现：
        1.查找指定编号的技能
        2.查找法力消耗大于10的所有技能
        3.查找技能冷却时间最小的技能
        4.根据法力消耗将序排列
        5.删除冷却时间大于10的技能
"""


class Skill():
    def __init__(self, id=0, name='', cost_sp=0, cd=0):
        self.id = id
        self.name = name
        self.cost_sp = cost_sp
        self.cd = cd

    def __repr__(self):
        return 'Skill(%d,"%s",%d,%d)' % (self.id, self.name, self.cost_sp, self.cd)


list_skill = [
    Skill(101, 's1', 5, 5),
    Skill(102, 's2', 20, 10),
    Skill(103, 's3', 15, 18),
    Skill(104, 's4', 12, 15),

]

from common.list_tools import ListHelper

# re01 = ListHelper.frist(list_skill,lambda i:i.id == 104)
# print(re01)

# re02 = ListHelper.find_all(list_skill,lambda i:i.cost_sp >= 10)
# for item in re02:
#     print(item)

# re03 = ListHelper.min(list_skill,lambda i:i.cd)
# print(re03)

# re04 = ListHelper.order_down(list_skill,lambda i:i.cost_sp)
# for item in list_skill:
#     print(item)

ListHelper.delete(list_skill, lambda i: i.cd >= 10)
for item in list_skill:
    print(item)
