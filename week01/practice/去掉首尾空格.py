# 去掉任意字符串首尾空格
name =input("输入字符串:")
count_1=count_2=0
for i in name:
    if " " == i :
        count_1 += 1
    else:
        break
for j in name[::-1]:
    if " " == j :
        count_2 += 1
    else:
        break
print(name[count_1:len(name)-count_2])
# 方法二
name = name.strip()
print(name)
