"""
    增删改查
"""

set01 = set()  # 注意：使用set = {}是创建字典
set01 = {1, 2, 3, 4, 2, 3}

# 列表转换为集合
set01 = set([1, 2, 3, 2, 3, 4, 5, ])
print(set01)

# 集合转换为列表
# 目的：去掉重复数值再转换为列表
list01 = list(set01)

# 添加元素
set01.add('a')
set01.add('b')
set01.add('a')
print(set01)

# 删除元素
# 不能删除没有的元素
set01.remove('a')
print(set01)

# 可以丢弃没有的元素
set01.discard('c')

"""
    计算
"""
s01 = {1, 2, 3}
s02 = {2, 3, 4}

# 交集
print(s01 & s02)  # {2,3}

# 并集
print(s01 | s02)  # {1,2,3,4}

# 补集
print(s01 - s02)  # {1}
print(s02 - s01)  # {4}

# 对称补集 相当于 (s01 - s02) | (s02 - s01)
print(s01 ^ s02)  # {1,4}

# s01 是 s02的 超集
# s02 是 s01的 子集
s01 = {1, 2, 3}
s02 = {2, 3}
print(s01 > s02)  # True
print(s01 < s02)  # False

# 集合推导式
numbers = [123, 3, 1, 4, 124, 1, 5, 1, 2, 3]
result = {i * 2 for i in numbers if i < 100}
print(result)

# 固定集合 -- 类似 元组 于 列表的区别
frozenset01 = frozenset(numbers)
print(frozenset01)
