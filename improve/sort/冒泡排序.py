"""
    冒泡排序
    重复走访要排序的数据，依次对比每两个相邻的元素，如果次序错误则交换位置
"""
import random
import time


def create_num(value, n):
    for i in range(n):
        value.append(random.randint(1, 200))


def bubble(value):
    for i in range(len(value) - 1):
        statu = False
        for j in range(len(value)-1-i):
            if value[j] > value[j+1]:
                value[j],value[j+1] = value[j+1],value[j]
                statu = True
        if not statu:
            return

if __name__ == '__main__':
    list1 = []
    create_num(list1, 10)
    bubble(list1)
    print(list1)

"""
10     1.2159347534179688e-05
100    0.0005357265472412109
1000   0.06183505058288574
10000  4.719357252120972
"""
