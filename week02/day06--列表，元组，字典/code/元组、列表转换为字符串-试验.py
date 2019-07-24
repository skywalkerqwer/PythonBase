dict1 = {'(1, 2)': 1}
a = (1, 2)
a = str(a)  # 元组用str转换为字符串第二个元素开始前面有一个空格
b = '(1, 2)'
c = [1, 2]  # 列表同理
c = str(c)
print(a, type(a), id(a))
print(b, type(b), id(b))
print(c, type(c), id(c))
print(a == b)
print(dict1[a])
print(dict1[b])
