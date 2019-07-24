"""
    为fun01/fun02添加计算时间的功能

import time

def fun01():
    time.sleep(1)
    print('fun01')
def fun02():
    time.sleep(1)
    print('fun02')
"""

import time

time_start = time.time()


def count_time(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        total_time = time.time() - time_start
        print(total_time)
        return result

    return wrapper


@count_time
def fun01():
    time.sleep(1)
    print('fun01')


@count_time
def fun02():
    time.sleep(1.5)
    print('fun02')


fun01()
fun02()
