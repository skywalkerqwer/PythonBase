class Person:
    def __init__(self):
        self.__name = 'zs'
        self.__money = 0
    #只读属性
    @property
    def name(self):
        return self.__name

    #只写属性
    def __set_money(self,value):
        self.__money = value

    money = property(None,__set_money)
