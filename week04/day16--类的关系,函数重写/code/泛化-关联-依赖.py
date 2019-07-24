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
    def __init__(self, name, job_object):
        """
        将员工共有的数据：姓名，底薪　在父类中定义
        :param name:
        :param base_salary:
        """
        self.name = name
        self.job_object = job_object
        #Staff 关联 job_object
        #Staff类中包含Job类成员

    def get_salary(self):
        """
            员工不要选择工资，由job负责计算工资的算法
            员工负责选择job
        :return:
        """
        return self.job_object.get_salary()

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


"""
    将程序员是一种员工的关系
    改变为
    程序员是一种岗位，员工有一个岗位是程序员
    将泛化关系转变为关联关系　　降低耦合度
"""

class Job():
    def __init__(self,base_salary):
        self.base_salary = base_salary

    def get_salary(self):
        return self.base_salary

# Job泛化Programmer
class Programmer(Job):
    def __init__(self, base_salary, dividends):
        super().__init__( base_salary)
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
        # 依赖是合作关系
        #Programmer的get_salary方法依赖于Job类的方法或数据

# Job泛化Testing
class Testing(Job):
    def __init__(self,  base_salary, bugs):
        super().__init__( base_salary)
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


class Sales(Job):
    def __init__(self, base_salary, sales):
        super().__init__(base_salary)
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

#创建：员工　叫小王　是一个程序员　工资是。。。
s01 = Staff('小王',Programmer(8000,5000))
# 转岗　改变员工职位，不改变员工自身信息
s01.job_object = Testing(5000,2000)