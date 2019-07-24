month = int(input("输入月份"))
if 1 <= month <= 12:
    if month <= 3:
        print("春")
    elif month <= 6:
        print("夏")
    elif month <= 9:
        print("秋")
    elif month <= 12:
        print("冬")
else:
    print("输入错误")
