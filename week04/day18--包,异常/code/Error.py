"""
    异常
"""


def div_apple(apple_count):
    person_count = int(input('输入人数：'))
    result = apple_count / person_count
    print('每人分了%d个苹果' % result)


# try:
#     div_apple(10)
# except Exception as e:
#     print('错误：',e)

# try:
#     div_apple(10)
# except ValueError:
#     print('输入有误')
# except ZeroDivisionError:
#     print('0不能做除数')
# except Exception:
#     print('未知错误')

try:
    div_apple(10)

except ValueError:
    print('输入有误')

except ZeroDivisionError:
    print('0不能做除数')

else:
    print('苹果分配成功')

finally:
    print('程序结束')
print('后续逻辑')
