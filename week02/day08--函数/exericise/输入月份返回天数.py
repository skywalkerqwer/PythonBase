"""
    根据月份返回天数
    要求：2月的闰年 29天
        平年 28天
"""
#不合适的方法：
# def get_day_by_month(year,month):
#     if month <1 or month >12:
#         return 0
#     if month == 2:
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             return 29
#         return 28
#     if month in (4,6,9,11):
#         return 30
#     return 31
def is_leap_year(year):
    """
    判断是否闰年
    :param year:
    :return:
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def get_day_by_month(year,month):
    """
    返回天数
    :param year:
    :param month:
    :return: 
    """
    if month <1 or month >12:
        return 0
    if month == 2:
        # if is_leap_year(year):
        #     return 29
        # return 28
        return 29 if is_leap_year(year) else 28
    if month in (4,6,9,11):
        return 30
    return 31