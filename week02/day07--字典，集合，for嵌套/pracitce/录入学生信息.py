"""
    在控制台中录入学生信息 内容如下
   info_student = [{'name':'zs','age':25,'score':100},{'name':'ls','age':35,'score':80}]
   将每个学生信息输出到控制台，每个学生一行
"""
list_info_student = []
n = 0
while True:
    dict_info_name = input('输入学生姓名:')
    if dict_info_name == '':
        break
    if dict_info_name not in list_info_student:
        list_info_student.append({})
        list_info_student[n]['name'] = dict_info_name
        dict_info_age = input("输入该学生年龄:")
        list_info_student[n]['age'] = dict_info_age
        dict_info_score = input("输入该学生成绩:")
        list_info_student[n]['score'] = dict_info_score
        n += 1
for i in range(len(list_info_student)):
    print('学生姓名：%s' % list_info_student[i]['name'], end=' ')
    print('年龄:%s' % list_info_student[i]['age'], end=' ')
    print('成绩：%s' % list_info_student[i]['score'])
