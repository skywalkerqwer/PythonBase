"""
    How are you --> you are How
"""

str_in = input("输入句子")
list = str_in.split(" ")
# 切片获取翻转列表，创建了新列表
str_out = " ".join(list[::-1])
# 反转列表,改变原列表
list.reverse()
list_out = ' '.join(list)
print(list_out)
print(str_out)
