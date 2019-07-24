"""
    自定义异常类
"""


# 自定义异常类的命名一般格式：XXXError,基类Exception
class AgeError(Exception):
    def __init__(self, code, msg):
        super().__init__(msg)
        self.code = code
        self.msg = msg


class Wife():
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 20 <= value <= 50:
            self.__age = value
        else:
            raise AgeError(22, '年龄错误')


try:
    w01 = Wife(99)
    print(w01.age)
except AgeError as error:
    print('错误原因：', error.msg)
    print('错误行数', error.code)
