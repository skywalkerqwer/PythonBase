"""
    定义函数：在控制台打印矩形
"""
def print_f(i,j,k):
    """
    打印 i 行 j 列 用 k 构成的矩形
    :param i:
    :param j:
    :return:
    """
    for item in range(i):
        print(k*j)

r = int(input("行："))
c = int(input("列："))
char = input("构成：")
print_f(r,c,char)

