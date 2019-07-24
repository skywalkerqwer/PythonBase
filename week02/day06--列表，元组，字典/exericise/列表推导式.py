"""
    使用列表推导式，生成1--10内的奇数和偶数列表
"""
# list_odd = [item for item in range(1, 11) if item % 2 != 0]
# print(list_odd)
# list_even = [item for item in range(1, 11) if item % 2 == 0]
# print(list_even)

"""
    [21,54,3,2,7,12,77] 获取列表中大于10的元素，组成新列表
"""
list_numbers = [21, 54, 3, 2, 7, 12, 77]
list_out = [number for number in list_numbers if number > 10]
print(list_out)

"""
    在控制台中输入一个起始值和一个终止值(不包含),
    将中间的整数存入一个列表，奇数存入另一个列表
"""
start = int(input("输入起始值："))
end = int(input("输入终止值："))
list_odd = [i for i in range(start, end) if i % 2 != 0]
list_even = [i for i in range(start, end) if i % 2 == 0]
print(list_odd)
print(list_even)
