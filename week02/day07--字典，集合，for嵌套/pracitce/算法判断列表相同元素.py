"""
    [1,4,7,5,7,9,4]
    设计一个算法判断列表中是否有相同元素
"""

list01 = [1,4,7,5,7,9,4]
# 假设没有相同元素
state = False
for i in range(len(list01) - 1):
    for j in range(i+1,len(list01)):
        if list01[i] == list01[j]:
            state = True
if state == True:
    print('Y')
else:
    print("N")