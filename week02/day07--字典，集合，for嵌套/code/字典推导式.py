"""
    字典推导式
"""
"""
    常规方法
"""
dic01 = {}
for item in range(1, 6):
    dic01[item] = item ** 2
print(dic01)

"""
    推导式方法
"""
# 语法 : {键  :    值     for 变量 in 可迭代对象 if 条件}
dic02 = {item: item ** 2 for item in range(1, 6)}
