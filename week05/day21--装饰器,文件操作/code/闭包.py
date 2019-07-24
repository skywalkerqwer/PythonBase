"""
    函数内部　定义函数

"""


# 压岁钱
def give_gift_money(money):
    print('获得%d元压岁钱' % money)

    def child_buy(target, price):
        nonlocal money
        if money >= price:
            money -= price
            print('购买成功，剩余%d元' % money)
        else:
            print('余额不足')

    # 返回内部方法　此时没有调用方法
    return child_buy


cb = give_gift_money(10000)
cb('九阳神功', 9000)
# cb('乾坤大挪移',8000)
cb('一阳指', 1000)
