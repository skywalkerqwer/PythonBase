"""
    根据成绩判断等级
    100--80 --> 优秀
    79--60  --> 良好
    60--0   --> 不合格
"""


def level(score):
    if score < 0 or score > 100:
        return 'Error'
    if score < 79:
        return 'A'
    return 'A+'


score = int(input('分数:'))
print(level(score))
