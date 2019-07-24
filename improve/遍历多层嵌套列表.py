list01 = [1, 2, [3, 4, [5, 6],7]]


def iter_list(list_target):
    for item in list_target:
        if isinstance(item, list):
            iter_list(item)
        else:
            print(item)


iter_list(list01)
