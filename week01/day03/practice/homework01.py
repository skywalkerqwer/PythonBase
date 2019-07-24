"""
    输入一个季度，输出该季度的月份
"""

# season = int(input("输入季度"))
# if season == 1:
#     print("1,2,3")
# elif season == 2:
#     print("4,5,6")
# elif season == 3:
#     print("7,8,9")
# elif season == 4:
#     print("10,11,12")
# else:
#     print("输入错误")


"""
    一个球从１００米高度落下，每次弹回原高度的一半，计算经过多少次最终落地（弹起高度小于0.01）
    总共经过多少米
"""
hight = 100
count = 0
path = hight
while True:
    if hight / 2 >= 0.01:
        hight /= 2
        path += hight * 2
        count += 1
    else:
        print("经过" + str(count) + "次落地" + "\n共经过" + str(path) + "米")
        break