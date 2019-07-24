side = int(input("矩形边长为："))
for i in range (1,side+1):
    for j in range(side):
        print("%d"%(j+i),end='')
    print("")