"""
    形参传递方式parameter
        命名关键字形参
"""


# 强制实参使用关键字传递
def fun1(*, a, b):
    print(a, b)


fun1(b=3, a=1)
fun1(**{'b': 2, 'a': 1})


def fun2(a, b, *, c=3, d=4):
    print(a, b, c, d)


fun2(1, 2, c=3, d=4)
fun2([1, 2], [3, 4])


def fun3(*args, c, d):
    print(args, c, d)


fun3(1, 2, 3, 4, 5, d=10, c=20)

# print函数定义
# print(*args, sep=' ', end='\n', file=None)
# 打印('内容',sep = '连接符',end = '结束符')
print(123, 'asd', 999, end='\n\n\n', sep='+')
# 双星号字典形参:可以收集多余的字典关键字形参
def fun4(**kwargs):
    print(kwargs)

fun4(a = 1,b = 2,c = 'abc',d=[1,2,3],e=True)


def fun5(*args,**kwargs):
    print(args,kwargs)

fun5()
fun5(1,3,'wqe',True,ddd=123,abc='qwe')