"""
    输入数字，判断是否为素数
"""
x = float(input("输入数字:"))
if x == 2:
    print("Y")
elif x>2 :
    for i in range(2, int(x)):
        if x % i == 0:
            print("N")
            break
        else:
            print("Y")
            break
else:
    print("N")
