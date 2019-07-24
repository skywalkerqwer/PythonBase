"""
    控制台中循环输入整数，当输入-1时退出。
    要求整数不能相同（相同就重输）
    计算：最大值 最小值 第二个最大值
"""
numbers=[]
number = 0
while True:
    number = int(input("输入整数："))
    if number == -1:
        break
    elif number in numbers:
        print('输入重复，重新输入:')
        continue
    else:
        numbers.append(number)
numbers.sort()
print(numbers)
print("最大值",max(numbers))
print("最小值",min(numbers))
print("第二个最大值",numbers[-2])
