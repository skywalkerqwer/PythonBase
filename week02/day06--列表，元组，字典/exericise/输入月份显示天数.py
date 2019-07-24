"""
    输入月份显示天数
"""
month = int(input("输入月份"))
tuple_day = (31,28,31,30,31,30,31,31,30,31,30,31)
print(tuple_day[month-1])
