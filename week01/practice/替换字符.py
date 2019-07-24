# for i in str_input:
#     for j in str_change:
#         if j!= str_input:
#             count_out += 1
#             if count_out == len(str_input):
#                 print("不存在字符:"+str_change)
#                 break
#             else:
#                 if i!=str_change:
#                     str_output += i
#                 else:
#                     str_output += str_change_to
# print(str_output)
str_input = input("输入字符串:")
str_change = input("将字符:")
str_change_to = input("替换为:")
str_output = ""
count_out = 0
for i in str_input:  # 在输入的字符串中寻找
    if i != str_change:  # 不是需要替换的字符
        count_out += 1  # 记录已经判断了几个字符
        str_output += i
    else:               # 需要替换的字符
        str_output += str_change_to
if count_out == len(str_input):  # 已经判断每个字符都不需要替换
    print("不存在字符:" + str_change)
else:
    print(str_output)
print(str_input.replace(str_change,str_change_to))#函数方法