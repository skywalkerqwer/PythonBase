s01 = 'abcde'
s02 = s01[::-1]
print(s02)
#
list_str=[]
for i in range(len(s01)):
    s01 =list(s01)
    list_str.append(s01.pop())
list_str = ''.join(list_str)
print(list_str)
#