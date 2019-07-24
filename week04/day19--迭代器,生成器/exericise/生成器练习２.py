"""
    定义函数my_zip实现下列代码
    zip()可将多个可迭代对象的元素组合成一个元组
    list01 = ['a','b','c']
    list02 = ['A','B','C']
    for item in zip(list01,list02):
        print(item)
"""


def my_zip(iter1, iter2):
    for i in range(len(iter1)):
        yield iter1[i], iter2[i]


list01 = ['a', 'b', 'c']
list02 = ['A', 'B', 'C']
for item in my_zip(list01, list02):
    print(item)
