# 创建字典
d01 = {}
d01 = dict()

# 创建具有默认值的字典
d01 = {'a':1,'b':2}

# 添加元素
# 如有没有key则添加
d01['c'] = 3

# 修改元素
# 有key则修改
d01['c'] = 4

# 删除元素
del d01['c']

# 查找元素
print(d01['a'])
if 'c' in d01:
    print(d01['c'])

# 查找所有
# 遍历字典---> 键
for key in d01:
    print(key)

# 遍历字典---> 值
for value in d01.values():
    print(value)

# 遍历字典---> 键-值对
for key_value in d01.items():
    print(key_value)
    # 分别拿 键 和 值
    print(key_value[0],key_value[1])

#字典不能 + *
# 用 **dict 拆分字典
d02 = {'d':6}
d03 = {**d01,**d02}  #先拆分字典再拼接成新字典
print(d02)
print(d03)