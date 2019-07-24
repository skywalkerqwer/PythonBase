import copy
import random
import time


def create_num(value, n):
    for i in range(n):
        value.append(random.randint(1, 200))


def bubble(value):
    for i in range(len(value) - 1):
        statu = False
        for j in range(len(value) - 1 - i):
            if value[j] > value[j + 1]:
                value[j], value[j + 1] = value[j + 1], value[j]
                statu = True
        if not statu:
            return


def insert_sort(value):
    for i in range(1, len(value)):
        temp = value[i]
        pos = i
        for j in range(i - 1, -1, -1):  # 从后向前扫描
            if temp < value[j]:
                value[j + 1] = value[j]
                pos = j
            else:
                pos = j + 1
                break
        value[pos] = temp


def quick_sort(value):
    if len(value) < 2:
        return value
    # 获取关键数据
    mark = value[0]
    smaller = [x for x in value if x < mark]
    larger = [x for x in value if x > mark]
    equal = [x for x in value if x == mark]
    return quick_sort(smaller) + equal + quick_sort(larger)


if __name__ == '__main__':
    list1 = []
    create_num(list1, 1000)
    list2 = copy.deepcopy(list1)
    list3 = copy.deepcopy(list1)

    t1 = time.time()
    bubble(list1)
    t2 = time.time()
    insert_sort(list2)
    t3 = time.time()
    l1 = quick_sort(list3)
    t4 = time.time()

    print(t2 - t1)
    print(t3 - t2)
    print(t4 - t3)
