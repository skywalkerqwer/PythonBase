time = int(input("输入秒数："))
for i in range(time, 0, -1):
    min = i // 60
    sec = i % 60
    print("%02d:%02d" % (min, sec))
