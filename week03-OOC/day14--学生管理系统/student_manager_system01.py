"""
    学生管理系统
"""


class StudentModel:
    """
    数据模型类
    """

    def __init__(self, id=0, name='', age=0, score=0):
        """
        创建学生对象
        :param id: 编号
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value


class StudentManageController:
    """
        逻辑控制类
    """

    def __init__(self):
        """
        创建学生管理器对象
        """
        self.__list_stu = []

    @property
    def list_stu(self):
        return self.__list_stu

    def __generate_id(self):
        """
        生成编号策略：在最后一个学生id基础上+1
                    第一个学生id设置为１
        :return:
        """
        return 1 if len(self.__list_stu) == 0 else self.__list_stu[-1].id + 1

    def add_student(self, stu):
        """
        添加学生对象
        :param stu:
        :return:
        """
        stu.id = self.__generate_id()
        self.__list_stu.append(stu)

    def remove_student(self, id):
        """
        依据id删除学生
        :param id:
        :return:
        """
        # self.__list_stu.pop(id-1)
        for item in self.__list_stu:
            if item.id == id:
                self.__list_stu.remove(item)
                return True
        return False

    def unpdate_student(self, stu_info):
        """
        修改学生信息
        :param stu_info: 学生信息
        :return:
        """
        for item in self.__list_stu:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        """
        在不改变原列表情况下排列
        需要用切片生成新列表
        :return:
        """
        list_order = self.__list_stu[:]
        for i in range(len(list_order) - 1):
            for j in range(i + 1, len(list_order)):
                if list_order[i].score < list_order[j].score:
                    list_order[i], list_order[j] = list_order[j], list_order[i]
        return list_order


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
            stu = StudentModel()
            stu.name = input('输入学生姓名:')
            stu.age = int(input('输入学生年龄:'))
            stu.score = int(input('输入学生成绩'))
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


view = StudentManagerView()
view.main()





# # 测试
# manager = StudentManageController()
# stu1 = StudentModel(name='zs', age=20, score=100)
# stu2 = StudentModel(name='ls', age=22, score=80)
# manager.add_student(stu1)  # 添加
# manager.add_student(stu2)  # 添加
# manager.remove_student(1)  # 删除
# manager.unpdate_student(StudentModel(2, 'ls', 25, 85))  # 修改
# for item in manager.list_stu:
#     print(item.id, item.name, item.age, item.score)
