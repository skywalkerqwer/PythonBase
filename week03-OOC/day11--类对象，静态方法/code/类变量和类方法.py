"""

"""


class ICBC():
    # 类变量:类的,被所有对象共享的数据
    moneys = 1000000

    def __init__(self, name, money):
        # 实例变量:对象的
        self.name = name
        self.money = money
        # 从总行中扣除当前支行消耗的钱
        ICBC.moneys -= money

    @classmethod
    def get_total_money(cls):
        # cls 指的是当前调用方法的类
        print(cls.moneys)


i01 = ICBC('广渠门支行', 100000)
ICBC.get_total_money()
i02 = ICBC('中关村支行', 200000)
ICBC.get_total_money()