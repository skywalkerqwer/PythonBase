"""
    输入季节返回月份
    春 夏 秋 冬 --> 1,2,3,...
"""
dict_season = {'春': "1月,2月,3月",
               '夏': '4月,6月,7月',
               '秋': '7月,8月,9月',
               '冬': '10月,11月,12月'
               }  # 用换行增加可读性
season = input("输入季节:")
print(dict_season[season])

