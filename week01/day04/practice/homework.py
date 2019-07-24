"""
    在控制台中输入一个长字符串，若改字符串中包含“qtx"，则显示”老师好“
"""
# str = input("输入：")
# if "qtx" in str:
#     print("老师好")
# else:
#     print("结束")

"""
    输入一个矩形边长，输出矩形
"""
# side = int(input("输入边长:"))
# high = side - 2
# wide = "*"+" "*high+"*\n"
# print("*"*side+"\n"+wide*high+"*"*side)

"""
    输入一个字符串，打印如下
    1.打印字符串第一个字符
    2.打印字符串最后一个内容
    3.如果长度是奇数则打印字符串中间内容  len()
"""
# str = input("输入字符串")
# print(str[:1])  # 打印第一个
# print(str[-1:])  # 打印最后一个
# if len(str) % 2 != 0:
#     print(str[len(str) // 2:len(str) // 2 + 1]) #打印中间字符
#
"""
    输入一个字符串，判断是否为回文，回文是中心对称的文字
"""
# str = input("输入字符串：")
# if len(str)>1:
#     if str == str[::-1]:
#         print("是回文")
#     else:
#         print("不是回文")
# else:
#     print("输入长度大于１的字符串")
"""
    输入一个字符串，将字符串的第一个字符和最后一个字符去掉
"""
# str = input("输入字符串")
# if len(str)>1:
#     print(str[1:len(str)-1])
# else:
#     print("请输入长度大于１的字符串")
