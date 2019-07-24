"""
    封装--私有化
    私有化实例变量：在变量名称前加双下划线
             本质：修改了变量名称
"""


class Wife01:
    def __init__(self, age, sex):
        # 数据
        # self.__age = age
        self.set_age(age)
        self.set_sex(sex)

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 20 <= value <= 30:
            self.__age = value
        else:
            raise ValueError('NO')

    def get_sex(self):
        return self.__sex

    def set_sex(self, value):
        self.__sex = value


w01 = Wife01(23, '女')
print(w01.__dict__)  # 存储对象的实例变量
w01.age = 32  # 视为添加新变量
w01.__age = 32  # 访问私有变量失败，因为私有变量名被修改
w01._Wife01__age = 100  # 可以修改私有变量的方法
w01.set_age(32)  # 正确的访问方式
print(w01.__dict__)
