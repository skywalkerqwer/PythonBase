"""
    穷尽一切手段，收集面向对象封装设计思想的资料，整理
    定义技能数据类（技能编号，技能名称，消耗发力，冷却时间，动画名称）
    使用属性进行封装，使用__slots__封装
"""


class Skill:
    __slots__ = ('__code','__name','__cd','__cost_sp','__action_name')
    def __init__(self, code = 0, name = '', cd = 0, cost_sp = 0, action_name = ''):
        self.code = code
        self.name = name
        self.cd = cd
        self.cost_sp = cost_sp
        self.action_name = action_name

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

    @property
    def action_name(self):
        return self.__action_name

    @action_name.setter
    def action_name(self, value):
        self.__action_name = value
