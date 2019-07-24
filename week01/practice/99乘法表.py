i = int(input("行:"))
j = int(input("列:"))
if i >= j:  # 判断输入的行数大于列数
    for col in range(1, i + 1):  # 逐行打印
        for row in range(1, j + 1):  # 在此行逐列打印
            if row <= col:  # 打印的此算式满足行>=列的条件
                print("%s*%s=%s\t" % (col, row, col * row), end='')
        print("")
else:
    print("输入错误")
