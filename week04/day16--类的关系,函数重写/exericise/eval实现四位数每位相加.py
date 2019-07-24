"""
    使用eval函数实现录入４位数实现每位相加
"""
num = input('四位数：')
re = eval('%s+%s+%s+%s'%(num[0],num[1],num[2],num[3]))
print(re)