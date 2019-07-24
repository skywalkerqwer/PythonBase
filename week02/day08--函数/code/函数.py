"""
    函数
    用于封装一个特定的功能，表示一个行为(用动词命名)
    可重复执行的语句块
"""


# 做函数
def attack():
    print('直拳')
    print('摆拳')
    print('勾拳')


# 调用函数
attack()

"""
    定义两个整数相加的函数
"""


# 做函数
def add(number01, number02):
    """
    两个整数相加
    :param number01: 第一个整数
    :param number02: 第二个整数
    :return:
    """
    result = number01 + number02
    return result


# 调用函数
num01 = int(input(""))
num02 = int(input(""))
re = add(num01, num02)  # re = result
print(re)
