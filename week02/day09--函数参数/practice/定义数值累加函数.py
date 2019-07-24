"""
    定义数值累加函数
"""

def get_sum_number(number_target=0):
    sum_number = 0
    for i in range(number_target+1):
        sum_number += i
    return sum_number

print(get_sum_number(4))