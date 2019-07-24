"""
    统计 hello 函数调用的次数
"""
def hello():
    global count
    count+=1

count = 0
hello()
hello()
hello()
hello()
hello()
hello()


print(count)