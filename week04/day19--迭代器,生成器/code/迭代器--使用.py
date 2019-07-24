"""
    迭代器－－使用
"""

list01 = [1, 32, 14, 1234, 987]
# for item in list01:
#   print(item)

"""
问：for循环原理:
      1.获取迭代器对象
      2.循环获取下一个元素
      3.遇到StopIteration停止迭代

可以被for的条件(什么是可迭代对象)：
      可以获取迭代器对象(具有__iter__方法)
"""


"""
# 1.获取迭代器对象
iterator = list01.__iter__()
# 2.获取下一个元素
item = iterator.__next__()
print(item)
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
# 3.直到错误　StopIteration
print(iterator.__next__()) #StopIteration
"""

iterator = list01.__iter__()
while True:
    try:
        print(iterator.__next__())
    except StopIteration:
        break
