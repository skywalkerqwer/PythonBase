str_in = input("输入字符串")
str_div = input("以该字符分割：")
str_out = ""
for j in str_in:
    if j != str_div:
        str_out += j
    else:
        str_out += "\t"
        continue
print(str_out)
# 函数法
print(str_in.split(str_div))