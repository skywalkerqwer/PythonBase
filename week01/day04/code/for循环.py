"""
    for range
"""

# for item in "hello world":
#     print(item)
# #     5 4 3 2 1
# for i in range(5,-1,-1):
#     print(i)
"""
    累加１－１００间偶数,跳过奇数
"""

sum = 0
for a in range(1, 101):
    if a % 2 == 0:
        sum+=a
    if a % 2 != 0:
        continue
print(sum)
