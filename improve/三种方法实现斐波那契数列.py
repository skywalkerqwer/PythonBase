"""
    递归实现斐波那契数列
"""


def fibo_1(n):
    """循环实现"""
    a, b = 1, 1
    l = []
    for i in range(n):
        l.append(a)
        a, b = b, a+b
    return l


def fibo_2(n):
    """递归实现"""
    if n<= 1:
        return 1
    else:
        return fibo_2(n-1) + fibo_2(n-2)

def fibo_3(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a+b

if __name__ == '__main__':
    print('循环实现：')
    res = fibo_1(5)
    print(res)

    print('\n递归实现：')
    for i in range(7):
        print(fibo_2(i), end=' ')

    print('\n\n生成器实现：')
    for i in fibo_3(9):
        print(i, end=' ')