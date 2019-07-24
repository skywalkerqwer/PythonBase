"""
    迭代器使用练习
    1.使用while +　迭代器　获取元组所有元素
    2.不使用for　获取字典所有元素
"""
tuple01 = ('悟空', '八戒', '唐僧', '沙僧', '女儿国国王')

dict01 = {'悟空': 2000, '八戒': 3000, '唐僧': 1000, '沙僧': 2800}

iterator_tuple = tuple01.__iter__()
while True:
    try:
        print(iterator_tuple.__next__())
    except:
        break

iterator_dict = dict01.__iter__()
while True:
    try:
        key = iterator_dict.__next__()
        print(key, dict01[key])
    except:
        break
