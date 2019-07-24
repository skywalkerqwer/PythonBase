"""
    定义获取成绩的方法
    要求：如果输入错误，重新录入
        成绩范围在0-100之间
"""


def get_score():
    while True:
        try:
            score = int(input('输入成绩'))
            if score < 0 or score > 100:
                raise ValueError
        except :
            print('输入0-100之间的数')
        else:
            return score

print(get_score())
