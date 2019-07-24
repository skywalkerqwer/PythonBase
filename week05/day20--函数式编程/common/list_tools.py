"""
    对列表常用操作模块
"""


class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target, func_condition):
        """
            查找符合条件的所有元素
        :param list_target: 对象列表
        :param func_condition: 查找条件
        :return:
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def frist(list_target, func_condition):
        """
            查找符合条件的第一个元素
        :param list_target: 对象列表
        :param func_condition: 查找条件
        :return:
        """
        for item in list_target:
            if func_condition(item):
                return item

    @staticmethod
    def count(list_target, func_condition):
        """
            按条件计数
        :param list_target: 对象列表
        :param func_condition: 计数条件
        :return:
        """
        count = 0
        for item in list_target:
            if func_condition(item):
                count += 1
        return count

    @staticmethod
    def max(list_target, func_condition):
        """
            按条件求最大值
        :param list_target: 对象列表
        :param func_condition:  查找条件
        :return:
        """
        value_max = list_target[0]
        for i in range(1, len(list_target)):
            if func_condition(value_max) < func_condition(list_target[i]):
                value_max = list_target[i]
        return value_max

    @staticmethod
    def min(list_target, func_condition):
        """
            按条件求最小值
        :param list_target: 对象列表
        :param func_condition: 查找条件
        :return:
        """
        value_min = list_target[0]
        for i in range(1, len(list_target)):
            if func_condition(value_min) > func_condition(list_target[i]):
                value_min = list_target[i]
        return value_min

    @staticmethod
    def sum(list_target, func_condition):
        """
            按条件求和
        :param list_target: 对象列表
        :param func_condition: 查找条件
        :return:
        """
        value_sum = 0
        for i in range(len(list_target)):
            value_sum += func_condition(list_target[i])
        return value_sum

    @staticmethod
    def select(list_target, func_condition):
        """
            按条件筛选对象
        :param list_target: 对象列表
        :param func_condition: 筛选条件
        :return:
        """
        for item in list_target:
            yield func_condition(item)

    @staticmethod
    def order_up(list_target, func_condition):
        """
            按条件进行升序排列
        :param list_target: 对象列表
        :param func_condition: 排序条件
        :return:
        """
        for i in range(len(list_target) - 1):
            for j in range(i + 1, len(list_target)):
                if func_condition(list_target[i]) > func_condition(list_target[j]):
                    list_target[i], list_target[j] = list_target[j], list_target[i]

    @staticmethod
    def order_down(list_target, func_condition):
        """
            按条件进行降序排列
        :param list_target: 对象列表
        :param func_condition: 排序条件
        :return:
        """
        for i in range(len(list_target) - 1):
            for j in range(i + 1, len(list_target)):
                if func_condition(list_target[i]) < func_condition(list_target[j]):
                    list_target[i], list_target[j] = list_target[j], list_target[i]

    @staticmethod
    def delete(list_target, func_condition):
        """
            删除元素
        :param list_target: 对象列表
        :param func_condition: 删除条件
        :return:
        """
        count = 0
        for i in range(len(list_target)-1,-1,-1):
            if func_condition(list_target[i]):
                del list_target[i]
                count += 1
        return count