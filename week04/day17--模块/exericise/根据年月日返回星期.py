import time


def get_week(year, month, day):
    tuple_time = time.strptime('%d/%d/%d' % (year, month, day), '%Y/%m/%d')
    weeks = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    return weeks[tuple_time[6]]


week01 = get_week(2019, 3, 20)
print(week01)
