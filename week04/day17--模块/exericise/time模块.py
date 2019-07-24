"""
    时间模块
"""


import time

# 返回时间戳(从1970年后到当前时间经过的秒数)
print(time.time())
print(time.time())

# 时间元组
# 时间戳 --> 时间元组
print(time.localtime(time.time()))

# 时间元组 -->时间戳
t01 = time.localtime(time.time())
print(time.mktime(t01))

# 格式化时间元组
# 年/月/日
print(time.strftime("%Y / %m / %d / %H / %M / %S",time.localtime()))

# 字符串 --> 时间元组
print(time.strptime('2019/03/20 17:32','%Y/%m/%d %H:%M'))



