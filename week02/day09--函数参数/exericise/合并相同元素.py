"""
0移动到末尾
合并相邻相同元素
"""
list_total = [2, 0, 2, 4]


def move_left(list_target):
    new_list = [item for item in list_target if item != 0]
    new_list += [0] * list_target.count(0)
    return new_list


def add_left(list_target):
    list_1 = move_left(list_target)
    for i in range(len(list_1) - 1):
        if  list_1[i] != 0 and list_1[i] == list_1[i + 1]:
            list_1[i] += list_1[i+1]
            list_1[i+1] = 0
    list_1 = move_left(list_1)
    return list_1

print(add_left(list_total))