"""
    while
"""
num01, num02 = int(input("输入第一个数")), int(input("输入第二个数"))
if num01 < num02:
    while num01 <= num02:
        print(num01)
        num01 += 1
elif num01 > num02:
    while num02 <= num01:
        print(num01)
        num01 -= 1
else:
    print(num01)