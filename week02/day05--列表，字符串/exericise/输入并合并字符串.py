"""
    循环输入字符，当输入q时退出并讲输入的字符串合并位一个字符串
"""
list = []
while True:
    str01 = input("输入字符")
    if str01 == 'q':
        break
    list.append(str01)
re = "".join(list)
print(re)