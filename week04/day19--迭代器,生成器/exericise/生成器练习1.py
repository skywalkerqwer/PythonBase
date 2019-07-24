"""
    用生成器实现

list01 = ['a','b','c']
for i in enumerate(list01):
    print(i[0],i[1])
"""
list01 = ['a','b','c']
def my_enu(list_target):
    index = 0
    for i in list_target:
        yield (index,i)
        index += 1

for item in my_enu(list01):
    print(item)