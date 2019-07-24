"""
    学生管理系统表示层
"""

from bll import StudentManageController
from models import StudentModel


class StudentManagerView:
    """
        学生管理器视图类
    """

    def __init__(self):
        """
        创建学生管理器控制对象
        """
        self.__controller = StudentManageController()

    def __display_menu(self):
        """
        显示菜单
        :return:
        """
        print('------------------------')
        print('1).添加学生')
        print('2).显示学生')
        print('3).删除学生')
        print('4).修改学生')
        print('5).按照成绩做降序显示')
        print('------------------------')

    def __select_menu(self):
        """
            选择菜单
        :return:
        """
        number = input('请输入选项：')
        if number == '1':
            self.__input_students()
        elif number == '2':
            self.__output_students(self.__controller.list_stu)
        elif number == '3':
            self.__delete_student()
        elif number == '4':
            self.__modify_student()
        elif number == '5':
            self.__output_students_by_score()

    def main(self):
        """
            学生管理器入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_students(self):
        while True:
            stu = self.input_info()
            self.__controller.add_student(stu)
            if input('按Y继续') != 'Y':
                break

    def __output_students(self, list_stu):
        """
        在控制台中输出所有学生对象信息
        :param list_stu: 需要显示的学生列表
        :return:
        """
        for item in list_stu:
            print('%d | %s | %d | %d' % (item.id, item.name, item.age, item.score))

    def __delete_student(self):
        while True:
            id = int(input('输入删除学生的id:'))
            if self.__controller.remove_student(id):
                print('删除成功')
            else:
                print('查无此人')
            if input('按Y继续') != 'Y':
                break

    def __modify_student(self):
        while True:
            stu_new = StudentModel()
            stu_new.id = int(input('输入要修改信息的学生id：'))
            stu_new.name = input('输入要修改信息的学生姓名：')
            stu_new.age = int(input('输入要修改信息的学生年龄：'))
            stu_new.score = int(input('输入要修改信息的学生成绩：'))
            if self.__controller.unpdate_student(stu_new):
                print('修改成功')
            else:
                print('查无此人')
            if input('按Y继续') != 'Y':
                break

    def __output_students_by_score(self):
        self.__output_students(self.__controller.order_by_score())


    def input_info(self):
        stu = StudentModel()
        stu.name = input('输入学生姓名:')
        while True:
            try:
                stu.age = int(input('输入学生年龄:'))
                if 6< stu.age<22:
                    break
            except:
                print('重新输入学生年龄')
        while True:
            try:
                stu.score = int(input('输入学生成绩'))
                if 0<stu.score<150:
                    break
            except:
                print('重新输入学生成绩')

        return stu
