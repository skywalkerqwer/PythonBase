def order_by(list_target):
    """
        队列表进行升序排列
    :param list_target:
    :return:
    """
    for i in range(len(list_target) - 1):
        for j in range(i + 1, len(list_target)):
            if list_target[i] > list_target[j]:
                list_target[i], list_target[j] = list_target[j], list_target[i]
    return list_target


def merge_list(list1, list2):
    """
        合并去重列表
    :param list1:
    :param list2:
    :return:
    """
    result = list1+list2
    for i in range(len(result)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if result[i] == result[j]:
                del result[i]
    return result

list1 = [1,3,5]
list2 = [2,4,6,8]
print(order_by(merge_list(list1,list2)))
