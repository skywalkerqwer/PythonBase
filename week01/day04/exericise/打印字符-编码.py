"""
    输入一个字符串，打印该字符串的每个字符编码。
"""
# str = input("输入字符")
# for i in str:
#     print(ord(i))

"""
    循环输入编码值，显示字符
"""
code = 0
while True:
    code = int(input("输入编码："))
    if code >= 0:
        print(chr(code))
    else:
        print("退出")
        break
