"""
    作业
    一家公司有如下几种岗位：
    程序员：底薪＋项目分红
    软件测试：底薪＋BUG数*5
    销售：底薪＋销售额*5％
    定义员工管理器：
                １．记录所有员工
                ２．计算所有员工总薪资
    要求：增加新的岗位，员工管理器满足开闭原则
        画出架构图，写出体现依赖倒置原则、开闭原则的点。
"""


class StaffManager():
    def __init__(self):
        self.__staffs = []

    def add_staffs(self, staff):
        if isinstance(staff, Staff):
            self.__staffs.append(staff)

    def get_salary(self, staff):
        if isinstance(staff, Staff):
            staff.get_salary()

    def get_total_salary(self):
        sum = 0
        for item in self.__staffs:
            sum += item.get_salary()
        return sum


class Staff():
    def __init__(self, name, base_salary):
        """
        将员工共有的数据：姓名，底薪　在父类中定义
        :param name:
        :param base_salary:
        """
        self.name = name
        self.base_salary = base_salary

    def get_salary(self):
        """
            将底薪统一管理
        :return:
        """
        return self.base_salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def base_salary(self):
        return self.__base_salary

    @base_salary.setter
    def base_salary(self, value):
        self.__base_salary = value


class Programmer(Staff):
    def __init__(self, name, base_salary, dividends):
        super().__init__(name, base_salary)
        self.dividends = dividends

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @property
    def dividends(self):
        return self.__dividends

    @dividends.setter
    def dividends(self, value):
        self.__dividends = value

    def get_salary(self):
        return super().get_salary() + self.dividends


class Testing(Staff):
    def __init__(self, name, base_salary, bugs):
        super().__init__(name, base_salary)
        self.bugs = bugs

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @property
    def bugs(self):
        return self.__bugs

    @bugs.setter
    def bugs(self, value):
        self.__bugs = value

    def get_salary(self):
        return super().get_salary() + self.bugs * 500


class Sales(Staff):
    def __init__(self, name, base_salary, sales):
        super().__init__(name, base_salary)
        self.sales = sales

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @property
    def sales(self):
        return self.__sales

    @sales.setter
    def sales(self, value):
        self.__sales = value

    def get_salary(self):
        return super().get_salary() + self.sales * 0.05


s01 = Testing('zs', 15000, 10)
s02 = Programmer('ls', 11000, 6000)
s03 = Sales('ww', 8000, 100000)
manager = StaffManager()
manager.add_staffs(s01)
manager.add_staffs(s02)
manager.add_staffs(s03)
print(manager.get_total_salary())
