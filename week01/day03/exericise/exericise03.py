month = int(input("输入月份"))
if 1 <= month <= 12:
    if month == 2:
        print("28")
    # elif month == 4 or month == 6 or month == 9 or month == 11:
    elif month in [4,6,9,11]:
        print("30")
    else:
        print("31")
else:
    print("输入错误")
