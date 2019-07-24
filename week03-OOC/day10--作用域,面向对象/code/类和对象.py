"""
    类和对象
"""


class Wife01:
    """老婆类"""

    # 备注:init方法，前后各有两个下划线
    def __init__(self, name, age, sex):
        # 数据
        self.name = name
        self.age = age
        self.sex = sex

    # 方法
    def cooking(self):
        print(self.name,'做饭')

w01 = Wife01('如花',20,'女')
w01.cooking()