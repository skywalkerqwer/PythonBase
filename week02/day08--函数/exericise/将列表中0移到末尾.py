"""
    定义函数：将列表中的 0 移动到末尾
    [2,0,2,0] --> [2,2,0,0]
"""


def move_0_to_end(list_input):
    """
    删0再补0
    :param list_input:
    :return:
    """
    for i in list_input:
        if i == 0:
            list_input.remove(0)
            list_input.append(0)
    return list_input


def zero_to_end(list_targer):
    """
    将非0元素构成新列表再补0
    :param list_targer:
    :return:
    """
    new_list = [item for item in list_targer if item != 0]
    new_list += [0] * list_targer.count(0)
    return new_list


print(move_0_to_end([2, 0, 2, 0]))
