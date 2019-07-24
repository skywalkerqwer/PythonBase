def judge_leap_year(year_input):
    result = (year % 4 == 0 and year % 100 != 0) \
             or year % 400 == 0

    return result

year = int(input("请输入年份："))
month = int(input("输入月份"))
day = int(input('输入日期'))
sum_day = 0
if 1<=month<=12:
    for i in range(1,month):
        if i == 2:
            if judge_leap_year(year):# 判断闰年
                sum_day += 29
            else:
                sum_day += 28
        elif i in [4,6,9,11]:
            sum_day += 30
        else:
            sum_day += 31
sum_day += day
print(sum_day)