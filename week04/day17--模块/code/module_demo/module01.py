"""
    提供功能的模块
"""
print('module01')

def fun1():
    print('module01 -- fun1')

class Myclass:
    def fun2(self):
        print('module -- fun2')

#  __name__ : 当前模块名称: __main__ / module01
if __name__ == '__main__':
    fun1()