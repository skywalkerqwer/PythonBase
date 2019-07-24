"""
    统计字符串内中文个数
"""


def count_Chinese(str_input):
    """
    统计字符串内中文个数
    :param str_input:
    :return:
    """
    count = 0
    for i in str_input:
        if 0x4E00 <= ord(i) <= 0x9FA5:
            count += 1
    return count


str_input = input('输入')
print(count_Chinese(str_input))
