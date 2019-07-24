"""
    增加验证权限的功能
"""


def verify(func):
    def wrapper(*args, **kwargs):
        print('验证')
        return func(*args, **kwargs)
    return wrapper


@verify
def enter_background():
    print('进入后台系统')


@verify
def delete_order(order_id):
    print('删除订单', order_id)


enter_background()
delete_order(1)
