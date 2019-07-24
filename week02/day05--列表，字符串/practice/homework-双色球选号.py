"""
    买彩票
    一注彩票：7个球（整数）
    6个红球：1-33（不能重复）
    1个篮球：1-16
    输出红球号码升序排序+蓝球号码
"""

list_numbers = []
while len(list_numbers) < 6:
    number_red = int(input("输入第%d个红球号码" % (len(list_numbers) + 1)))
    print(number_red)
    if number_red < 1 or number_red > 33:
        print("超出选号范围，请重新输入")
    elif number_red in list_numbers:
        print("请勿重复选号")
    else:
        list_numbers.append(number_red)
list_numbers.sort()
while True:
    number_blue = int(input("输入蓝球号码:"))
    if 1 <= number_blue <= 17:

        list_numbers.append(number_blue)
        break
    else:
        print("超出选号范围，请重新输入")
# 结果用列表表示
numbers = ''.join(str(list_numbers))
print(numbers)
# 结果用字符串表示
result_list = []
for i in list_numbers:
    result_list.append(str(i))
result = ' '.join(result_list)
print(result)
