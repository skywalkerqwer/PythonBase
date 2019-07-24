"""
    1,2,3,4能组成多少个互不相同切不重复的三位数,各是多少
"""
# num = num_100 = num_10 = num_1 = 0
# count = 0
# for a in range(1, 5):
#     num_100 = a * 100
#     for b in range(1, 5):
#         num_10 = b * 10 + num_100
#         for c in range(1, 5):
#             num_1 = c + num_10
#             if str(num_1)[0:1] != str(num_1)[1:2] and str(num_1)[0:1] != str(num_1)[2:3] and str(num_1)[1:2] != str(num_1)[2:3]:
#                 print("%d\t" % num_1, end='')
#                 count += 1
#             else:
#                 continue
#         print("")
# print("有%d组排列" % count)

count = 0
for a in range(1, 5):  # 遍历百位
    for b in range(1, 5):  # 遍历十位
        for c in range(1, 5):  # 遍历个位
            if (a != b) and (b != c) and (a != c):  # 判断满足没有重复数字的条件
                num = a * 100 + b * 10 + c  # 个十百位组成一个３位数
                print("%d\t" % num, end='')
                count += 1  # 记录一种满足条件的排列组合
        print("")
print("有%d组排列" % count)
