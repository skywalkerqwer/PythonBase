# 判断开头
str = input("输入字符串")
str_start = input("开头是否为：")
count_start = 0
for i in str:
    if len(str_start) >= count_start + 1:#判断次数为输入要判断的开头的字符长度
        if i != str_start[count_start:count_start + 1]:#有一个字符不同则判断为不同
            print("不是")
            break
        else:
            count_start += 1#记录判断次数
    print("是")
    break
# 判断结尾
str_end = input("结尾是否为：")
count_end = 1
for j in str[::-1]:
    if len(str_end) >= count_end:#比较次数为输入要判断的开头的字符长度
        if j != str_end[-1 * count_end:-1 * count_end - 1:-1]:#有一个字符不同则判断为不同
            print("不是")
            break
        else:
            count_end += 1#记录判断次数
    print("是")
    break
