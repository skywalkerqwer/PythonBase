"""
    內建函数重写
"""


class Wife:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 对象转换的字符串(给人看的)
    def __str__(self):
        return 'OK'

    # 对象转换的字符串(给程序看的)
    def __repr__(self):
        return "Wife('%s',%d)" % (self.name, self.age)


w01 = Wife('铁锤', 26)
print(w01)  # print 内部使用__str__返回的字符串
list01 = [w01]
print(list01)  # print列表时　内部使用的是__repr__返回对象字符串
# eval方法可以将字符串转换为程序语句
w02 = eval("Wife('铁锤',26)")
print(w02.name)
w03 = eval(repr(w01))
# w03 = eval(w01.__repr__())
print(w03.name)
