list01 = [2,5,7,9,4]
# 传统生成列表写法
list_result = []
for item in list01:
    list_result.append(item ** 2)
print(list_result)
# 列表推导式写法
list_result = [item **2 for item in list01]
print(list_result)

# 传统生成列表写法
list_result = []
for item in list01:
    if item % 2 == 0:
        list_result.append(item ** 2)
print(list_result)
# 列表推导式写法
list_result = [item ** 2 for item in list01 if item % 2 == 0]
print(list_result)
"""
    语法：
    变量 = [逻辑处理 for 变量 in 可迭代对象 if 条件]
"""