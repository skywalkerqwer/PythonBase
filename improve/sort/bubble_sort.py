"""
    冒泡排序
"""
import time



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


list01 = [3, 2, 1, 7, 8, 9]
list02 = [3, 2, 1, 7, 8, 9]
time1 = time.time()

fun_sort_1(list01)

time2 = time.time()

fun_sort_2(list02)

time3 = time.time()

print(list01,time2-time1)
print(list02,time3-time2)
