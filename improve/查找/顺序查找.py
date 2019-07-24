"""
    算法是计算机为解决特定的问题而产生的一系列解决问题的清晰指令
    也就是对解决方案的准确而完整的描述

"""
"""
    顺序查找：从待查找数据中第一个元素开始，逐个对每个元素进行对比
    54张扑克牌只取红桃1-13，洗牌后查找红桃7
"""

def linear_1(value,key):
    for i,num in enumerate(value):
        if num == key:
            return i
    else:
        return -1




def linear(list_target, target):
    for i in range(len(list_target)):
        if target == list_target[i]:
            return i
    return -1

if __name__ == '__main__':
    listRed = [6, 12, 7, 3, 9, 2, 4, 5, 11, 8, 1, 13, 10]
    key = 7
    res = linear_1(listRed, key)
    if res == -1:
        print('查找失败')
    else:
        print(res)