"""
    斐波那契数列
"""
list = [1, 1]
for i in range(1, 21):
    list.append(list[i - 1] + list[i])
print(list)
