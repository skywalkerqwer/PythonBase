"""
    [[2048],[8402],[1024],[4201]]
"""

list_total = [[2, 0, 2, 4], [0, 4, 4, 0], [0, 4, 2, 0], [2, 4, 0, 4]]


def print_total(list_total):
    for i in range(len(list_total)):
        print(list_total[i])


def move_left(list_total):
    for i in range(4):
        for j in list_total[i]:
            if j == 0:
                list_total[i].remove(0)
                add_left(list_total[i])
                list_total[i].append(0)
        add_left(list_total[i])
        list_total[i].remove(0)
        list_total[i].append(0)
    return list_total


def add_left(list_total):
    for k in range(len(list_total) - 1):  # 加
        if list_total[k] == list_total[k + 1]:
            list_total[k] += list_total[k + 1]
            list_total[k + 1] = 0
    return list_total


print_total(list_total)
while True:
    action = input('下一步: ')
    if action == 'a':
        print_total(move_left(list_total))
