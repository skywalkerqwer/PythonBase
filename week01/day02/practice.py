"""
    使用二进制输出1  3   5
        八进制  1  8  10
         十六进制  1  13  20
"""
print(0b01, 0b11, 0b101)
print(0o1, 0o10, 0o12)
print(0x1, 0xd, 0x14)
"""
    输入圆的半径，输出面积周长
"""
r = int(input("输入圆的半径："))
s = 3.14 * r ** 2
c = 2 * 3.14 * r
print("圆的面积为" + str(s) + "\n圆的周长为" + str(c))

"""
    输入总秒数，计算几小时零几分钟零几秒钟。
"""
int_sec = int(input("输入总秒数:"))
hour = str(int_sec // 3600)
min = str(int_sec % 3600 // 60)
sec = str(int_sec % 60)
print(hour + "时" + min + "分" + sec + "秒")
