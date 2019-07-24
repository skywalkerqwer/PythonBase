"""
    生成器表达式
"""

list01 = [2,3,4,5]
# 列表推导式
# 内存中存储所有数据
list02 = [item **2 for item in list01]

# 生成器表达式
# 执行过后，没有计算结果
g03 = (item ** 2 for item in list01)
print(g03)
for item in g03:
    print(item)