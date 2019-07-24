# import random
#
# number = random.randint(1, 101)
# num = int(input("猜数字为："))
# count = 1
# while num != number:
#     while num < number:
#         while num < number:
#             print("小")
#             num = int(input("再猜数字为："))
#             count += 1
#     while num > number:
#         while num > number:
#             print("大")
#             num = int(input("再猜数字为："))
#             count += 1
# else:
#     print("数字为：" + str(number))
#     print("正确！共猜了" + str(count) + "次")

import random

number = random.randint(1, 101)
count = 0
while count<=6 :
    count += 1
    input_number = int(input("猜数字为："))
    if input_number > number:
        print("大")
    elif input_number < number:
        print("小")
    else:
        print("数字为：" + str(number))
        print("正确！共猜了" + str(count) + "次")
        break
else:
    print("失败！６次未猜中")

