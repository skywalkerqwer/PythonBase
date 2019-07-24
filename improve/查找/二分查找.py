"""
    二分查找：
        前提：有序数据（升序）
        由中间元素将数据分为左右两部分，比较中间元素与待查找值的大小
        如果相等 则查找成功
        如果中间元素比目标元素大，则继续在左侧重复该过程
        如果中间元素比目标元素小，则继续在右侧重复该过程
        如此递归下去直到成功找到或者查找完所有数据为止
"""


def binary(value, key, left, right, count=0):
    """

    :param value: 有序列表
    :param key: 目标值
    :param left: 左侧边界
    :param right: 右侧边界
    :return:
    """
    if left > right:
        # 查找失败
        return -1, count
    middle = (left + right) // 2
    if value[middle] == key:
        count += 1
        return middle, count
    elif value[middle] > key:
        count += 1
        return binary(value, key, left, middle - 1, count)
    elif value[middle] < key:
        count += 1
        return binary(value, key, middle + 1, right, count)


if __name__ == '__main__':
    list1 = [i for i in range(1,133)]
    print(list1)
    res = binary(list1, 1, 0, len(list1))
    print(res)
