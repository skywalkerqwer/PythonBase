"""
    字典推导式
"""
"""
练习一： 
有一个字符串列表:['12','asd','tarena']
       生成字典:{'12':2,'asd':3,'tarena':6} 键为字符长度
"""
# list01 = ['12','asd','tarena']
# dict01 = {i : len(i) for i in list01 }
# print(dict01)

"""
    输入任意字符再组成列表?
"""
list02 = []
i = 0
while True:
    item = input("")
    if item == " ":
        break
    else:
        list02.append(item)  # 组成列表用append叠加
        i += 1
dict02 = {i: len(i) for i in list02}
print(dict02)

"""
    练习二：[101,102,103]
           ['zs','ls','ww']
      合成:{101:'zs',102:'ls','103':'ww'}
"""
# list_01 = [101, 102, 103]
# list_02 = ['zs', 'ls', 'ww']
# dict03 = {list_01[i]:list_02[i] for i in range(len(list_01))}
# print(dict03)
