"""
    继承
    架构设计
    --老张开车去东北
    需求变化：可能坐飞机/火车/……
"""


class Person:
    # 违反面向对象设计原则
    # 开闭原则：　对扩展开放　　对修改关闭
    # 　　　　　　增加新功能　不要修改以前的代码
    # 依赖倒置： 使用抽象(父类)
    #           调用者使用父类成员而无视子类
    """
    def go_home(self, way):
        if way == '火车':
            print('呜－－')
        if way == '汽车':
            print('滴－－')
        #增加新功能
        if way == '飞机':
            print('嗖－－')
    """

    def go_home(self, way):
        # 如果传入对象不是交通工具则退出方法
        if not isinstance(way, Vehicle):
            return
        way.transport()


class Vehicle():
    def transport(self):
        # 人为抛出一个未实现错误
        # 目的：要求子类必须具有当前方法
        raise NotImplementedError


class Train(Vehicle):
    """
        火车类
    """

    # def move(self):
    #     print('呜－')
    # 统一行为
    def transport(self):
        print('呜－')


class AirPlain(Vehicle):
    """
        飞机类
    """

    # def fly(self):
    #     print('嗖－')
    # 统一行为
    def transport(self):
        print('嗖－')


class Car(Vehicle):
    """
        增加汽车类
    """

    def transport(self):
        print('滴－')


# 测试
p01 = Person()
p01.go_home(AirPlain())
p01.go_home(Train())
p01.go_home(Car())
