"""
    使用代码描述一下场景：
    张三 教 李四 学 王者荣耀
    李四 教 张三 学 Python
    李四 上班赚了 5000元
    最后输出：张三具有的技能，李四具有的技能，以及他们的钱
"""


class Person:
    def __init__(self, name, money=0):
        self.name = name
        self.money = money
        self.skill = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    @property
    def skill(self):
        return self.__skill

    @skill.setter
    def skill(self, value):
        self.__skill = value

    def earn_money(self, value):
        print('%s 挣了 %d' % (self.name, value))
        self.money += value

    def teach(self, person, skill):
        print('%s　教　%s　%s' % (self.name, person.name, skill))
        person.skill.append(skill)


zs = Person('张三')
ls = Person('李四')

zs.teach(ls, '王者荣耀')
print('张三会:', zs.skill)
print('李四会:', ls.skill)

ls.teach(zs, 'Python')
print('李四会:', ls.skill)
print('张三会:', zs.skill)

ls.earn_money(5000)
print('李四有:', ls.money)
