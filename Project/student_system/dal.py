"""
    Data
    Access
    Layer

1.保存学生列表(由bll层的添加/删除/修改方法调用)
2.加载学生列表(bll层Controller类的构造函数)
"""
FILE_PATH = "list_stu.txt"
from models import StudentModel
import os

class TextDao:
    """
        文本文件　数据访问对象
    """
    @staticmethod
    def save_student_list(list_stu):
        with open("FILE_PATH","w",encoding="utf-8") as stu_file:
            for stu in list_stu:
                stu_file.write(stu.__repr__()+'\n')

    @staticmethod
    def load_student_list():
        list_stu = []
        if not os.path.isfile(FILE_PATH):
            return list_stu
        with open(FILE_PATH, 'r', encoding='utf-8') as stu_file:
            for line in stu_file:
                list_stu.append(eval(line))
        return list_stu

