"""
    拼接
"""
# 每次拼接产生一个新对象
# re = []
# for item in range(1,6):
#     re += str(item)
# print(re)
# 3次以上拼接使用下列方法
list = []
for item in range(1,6):
    list.append(str(item))
result = "".join(list)
print(result)

"""
    拆分
"""
str01 = '1b2b3b4b'
re_str = str01.split('b')
print(re_str)