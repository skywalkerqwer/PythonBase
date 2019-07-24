"""
    定义学生类，自定义异常，返回成绩错误信息
"""


class ScoreError(Exception):
    def __init__(self, code, msg):
        super().__init__(msg)
        self.code = code
        self.msg = msg


class Stdent():
    def __init__(self, score):
        self.score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ScoreError(23, '成绩错误')


try:
    s01 = Stdent(200)
    print(s01.score)
except ScoreError as e:
    print('错误原因:', e.msg)
    print('错误代码位置:', e.code)
