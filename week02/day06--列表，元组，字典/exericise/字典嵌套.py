"""
    字典嵌套字典
"""
cities = {'Beijing': {'country': 'China', 'population': 20000000},
          'NewYork': {'country': 'U.S.A', 'polulation': 18000000}}

print(cities['Beijing']['population'])  # 获取北京的人口
print(cities['NewYork'])  # 获取纽约的城市信息
"""
    字典嵌套列表、元组
"""
d01 = dict([('a', 1), ('b', 2)])
print(d01)
d02 = dict((('c', 1), ('d', 2)))
print(d02)
