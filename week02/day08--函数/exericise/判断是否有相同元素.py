"""
    定义函数：判断列表是否具有相同元素
"""


def judge(list):
    """
    判断list内是否具有相同元素
    :param list:
    :return:
    """
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return True
    return False


list01 = [1, 4, 7, 1, 7, 9, 4]
list02 = [1, 2, 3, 4, 5, 6, 7]
if judge(list01):
    print('Y')
else:
    print("N")
if judge(list02):
    print('Y')
else:
    print("N")
