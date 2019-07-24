"""
    形参传递方式
"""


# 位置形参
def fun1(a, b, c):
    pass


# 星号元组形参
def fun2(*args):
    # 对于函数而言，args就是元组
    print(args)


fun2()
fun2(1)
fun2(1, 2)
fun2(*{1:'a',2:'b',3:'c'})
fun2(**{1:'a',2:'b',3:'c'})
