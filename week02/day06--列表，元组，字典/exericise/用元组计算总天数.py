"""
    计算某月某日是这一年的第几天
"""
month_in = int(input("输入月份"))
day_in = int(input("输入日期"))
month_31 = (1,3,5,7,8,10,12)
month_30 = (4,6,9,11)
sum_day = 0
# 循环方法
for month in range(1,month_in):
    if month in month_31:
        sum_day += 31
    elif month in month_30:
        sum_day += 30
    else:
        sum_day += 28
sum_day += day_in
print(sum_day)
# 容器方法
tuple_day = (31,28,31,30,31,30,31,31,30,31,30,31)
sum_day = sum(tuple_day[:month_in-1]) + day_in
print(sum_day)