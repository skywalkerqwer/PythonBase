"""
    将数据插入到已经有序的部分中
    前提条件：首元素默认有序
"""


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


if __name__ == '__main__':
    l1 = [5, 123, 51, 132, 4, 6, 3, 23, 41]
    insert_sort(l1)
    print(l1)
