str = input("输入字符串")
# for实现
count_for = 0
for i in str:
    if " " == i:
        count_for += 1
# while实现
count_while = 0
j = 0
while j < len(str):
    str_temp = str[j:j + 1]
    j += 1
    if " " == str_temp:
        count_while += 1
print(count_for,count_while)

print(str.count(" "))#函数实现