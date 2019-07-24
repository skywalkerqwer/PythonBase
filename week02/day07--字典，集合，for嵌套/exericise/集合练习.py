"""
    重复输入内容，统计输入次数，打印不重复的内容
"""
# set01 = set()
# n = 0
# while True:
#     str_input = input("输入内容：")
#     if str_input != ' ':
#         set01.add(str_input)
#         n+=1
#     else:
#         break
# print(set01)
# print("输入%d次"%n)

"""
    经理：曹操，刘备，孙权
    技术员：曹操，刘备，张飞，关羽
    使用2个列表list分别存储经理与技术员
    使用集合计算：
            1.既是经理又是技术员的
            2.是经理但不是技术员的
            3.是技术员但不是经理的
            4.张飞是经理吗
            5.身兼一职的都有谁
            6.经理和技术员共有几个人
"""
list_manager = ['曹操', '刘备', '孙权']
list_tech = ['曹操', '刘备', '张飞', '关羽']
set_manage = frozenset(list_manager)
set_tech = frozenset(list_tech)
print(set_manage & set_tech)
print(set_manage - set_tech)
print(set_tech - set_manage)
print('张飞' in set_manage)
print(set_tech ^ set_manage)
print(len(set_tech | set_manage))
super