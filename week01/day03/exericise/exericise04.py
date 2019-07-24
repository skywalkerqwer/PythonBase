"""
    一
"""
num = int(input("输入一个数："))
if num % 2:
    print("奇数")
else:
    print("偶数")

"""
    二－１
"""
year = int(input("请输入年份："))
result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# if not year % 4 and year % 100 or not year % 400:
if result:
    print("29")
else:
    print("28")

"""
    二－２
"""
year = int(input("请输入年份："))
day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
print(day)