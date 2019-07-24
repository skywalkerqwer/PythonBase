admin = "admin"
password = "123456"
time = 3
while time != 0:
    input_admin = input("输入账户名:")
    input_password = input("输入密码:")
    if input_admin == admin and input_password == password:
        print("登录成功")
        break
    else:
        time -= 1
        print("输入错误\n还剩"+str(time)+"次机会")
else:
    print("登录失败")