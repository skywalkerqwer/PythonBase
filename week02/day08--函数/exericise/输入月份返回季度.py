
"""
    定义函数：根据月份返回季度
"""


def season(month):
    """
    输入月份返回季度
    :param month:
    :return:
    """
    dict_season = {(1, 2, 3): '春', (4, 5, 6): '夏', (7, 8, 9): '秋', (10, 11, 12): '冬'}
    for i in dict_season:
        if month in i:
            return dict_season[i]
    return None
def get_season(month):
    """
    逻辑判断
    :param month:
    :return:
    """
    if month<1 or month >12:
        return None
    if month<=3:
        return '春天'
    if month<=6:
        return '夏天'
    if month<=9:
        return '秋天'
    return '冬天'

month_input = int(input("月："))
print(season(month_input))
print(get_season(month_input))