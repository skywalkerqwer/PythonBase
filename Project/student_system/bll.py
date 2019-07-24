"""
    学生管理系统业务逻辑层
    Busines
    Logic
    Layer
"""
from dal import TextDao


def save_data(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # 在类外访问私有变量,必须使用_类名__变量名
        TextDao.save_student_list(args[0]._StudentManageController__list_stu)
        return result
    return wrapper


class StudentManageController:
    """
        逻辑控制类
    """

    def __init__(self):
        """
        创建学生管理器对象
        """
        self.__list_stu = TextDao.load_student_list()

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

    @save_data
    def add_student(self, stu):
        """
        添加学生对象
        :param stu:
        :return:
        """
        stu.id = self.__generate_id()
        self.__list_stu.append(stu)

    @save_data
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

    @save_data
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
