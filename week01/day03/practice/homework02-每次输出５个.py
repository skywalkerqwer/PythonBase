# begin, end = int(input("输入第一个数")), int(input("输入第二个数"))
# if begin < end:
#     while begin <= end:
#         print(begin)
#         begin += 1
# elif begin > end:
#     while end <= end:
#         print(begin)
#         begin -= 1
# else:
#     print(begin)

begin, end = int(input("输入第一个数")), int(input("输入第二个数"))
if begin < end:
    for x in range(begin, end + 1):
        print("%5d" % x, end='')
        if (x % 5 == 0):
            print("")
else:
    for x in range(end, begin + 1):
        print("%5d" % x, end='')
        if (x % 5 == 0):
            print("")
