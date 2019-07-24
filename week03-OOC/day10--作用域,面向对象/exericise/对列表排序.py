"""
    定义对列表list排序的方法
"""


def fun_sort_1(list_target, i=0):
    while i < len(list_target) - 1:
        if list_target[i] > list_target[i + 1]:
            list_target[i + 1], list_target[i] = list_target[i], list_target[i + 1]
            i = 0
        else:
            i += 1
# return list_target 不需要return


def fun_sort_2(list_target):
    for i in range(len(list_target) - 1):
        for j in range(i + 1, len(list_target)):
            if list_target[i] > list_target[j]:
                list_target[i], list_target[j] = list_target[j], list_target[i]
# return list_target 不需要return


list01 = [2, 8, 6, 1, 3, 9]
list02 = [4, 5, 1, 9, 4, 7]
fun_sort_1(list01)
fun_sort_2(list02)
print(list01)
print(list02)
