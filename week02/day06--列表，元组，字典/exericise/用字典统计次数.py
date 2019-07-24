"""
    输入一段文字，打印出现的字符及次数
    "abcaabc" -->
    a --> 3
    b --> 2
    c --> 2
"""
str_in = input("输入字符串")
dict01 = {}
for i in str_in:
    if i not in dict01:  # 该字符第一次出现
        dict01[i] = 1
    else:  # 出现次数+1
        dict01[i] += 1
for key in dict01:
    print('字符:%s --> 出现次数：%d'%(key,dict01[key]))