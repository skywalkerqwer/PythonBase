# 外层控制行
for r in range(3):
    # 内层控制列
    for c in range(4):
        print('*', end='')
    print()
"""
    列表推导式
"""

list01 = ['1','2','3']
list02 = ['A','B','C']
result = [r+c for r in list01 for c in list02]
print(result)