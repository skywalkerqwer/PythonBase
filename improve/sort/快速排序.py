"""
    任取一个数据（第一个）作为关键数据
    将所有比关键数据小的放在它左侧，比它大的放在右侧
"""


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
    l1 = [54, 87, 61, 321, 84, 47, 73, 16, 87, 3]
    l2 = quick_sort(l1)
    print(l2)