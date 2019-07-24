"""
练习一：
    *****
    #####
    *****
    #####
"""
# for k in range(2):
#     for i in range(5):
#         print('*', end='')
#     print()
#     for j in range(5):
#         print('#', end='')
#     print()

"""
练习二：
    *
    **
    ***
    ****
"""
# 方法一
# for i in range(1,5):
#     print('*'*i,end='')
#     print()

# 方法二
for i in range(4):
    for j in range(i+1):
        print('*', end='')
    print()

"""
    ****
     ***
      **
       *
"""
for i in range(4,0,-1): # 4,3,2,1
    for k in range(4-i):
        print(' ',end='')
    for j in range(i):
        print("*",end='')
    print()

"""
    列表推导式
    两个列表全排列
"""
list01 = ['香蕉','苹果','哈密瓜']
list02 = ['牛奶','咖啡','雪碧']
result = [i+j for i in list01 for j in list02]
print(result)