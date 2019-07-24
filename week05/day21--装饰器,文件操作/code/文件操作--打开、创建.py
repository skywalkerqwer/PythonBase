"""
    文件操作
     1.创建一个文件，写入hello world
     open('路径','操作模式',encoding='utf-8')
"""

"""
my_file = None
try:
    my_file = open('my_file01.txt', 'w', encoding='utf-8')  # w 是覆盖写
    my_file.write('hello world')
finally:
    if my_file != None:  # 文件不是空则关闭
        my_file.close()
"""

"""""
with open('my_file01.txt', 'w', encoding='utf-8') as my_file:
    my_file.write('hello world')
"""

"""
    创建多个嵌套文件夹
"""
import os
if not os.path.isdir('file_demo'):
    os.makedirs('file_demo')

with open('file_demo/my_file01.txt', 'w', encoding='utf-8') as my_file:
    my_file.write('hello world')
