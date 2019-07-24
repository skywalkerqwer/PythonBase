"""
    定义方法，计算指定范围内的素数
"""


#
# def prime_numbers(begin, end):
#     list_prime = []
#     for i in range(begin, end + 1):
#         if i > 1:
#             for j in range(2, i):
#                 if i % j == 0:
#                     break
#             else:
#                 list_prime.append(i)
#
#     return list_prime
#
#
# print(prime_numbers(1, 20))

def is_prime(number):
    if number < 2:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            return True


def get_prime(begin, end):
    # list_prime = []
    # for number in range(begin,end):
    #     if is_prime(number):
    #         list_prime.append(number)
    list_prime = [number for number in range(begin, end) if is_prime(number)]
    return  list_prime


L = get_prime(10,20)
print(L)
