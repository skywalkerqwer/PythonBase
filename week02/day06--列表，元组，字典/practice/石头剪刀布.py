"""
        石头  剪刀  布
输入代表：0    1    2
根据游戏规则显示：平局 胜利 失败
"""

"""
    方法一
"""
# import random
#
# dict_1 = {'02': "输", '01': '赢', '10': '输', '12': '赢', '21': '输', '20': '赢'}
# AI_number = input("出:石头(0)、剪刀(1)、布(2) ")
# Player_number = str(random.randint(0, 2))
# dict_game = {'0': '石头', '1': '剪刀', '2': '布'}
# print("玩家:%s  电脑:%s" % (dict_game[AI_number], dict_game[Player_number]))
# if Player_number != AI_number:
#     print(dict_1[AI_number + str(Player_number)])  # 注意：用变量指代键时不能加引号
# else:
#     print('平')
#
"""
    方法二
"""
# wins = ('石头', '剪刀'
#               '剪刀', '布'
#                     '布', '石头')
# item = ('石头', '剪刀', '布')
# import random
#
# AI_input_number = random.randint(0, 2)
# AI_input = item[AI_input_number]
# player_input_number = int(input("出:石头(0)、剪刀(1)、布(2) "))
# player_input = item[player_input_number]
# print('玩家：%s  电脑:%s'%(item[player_input_number],item[AI_input_number]))
# item_input = (AI_input, player_input)
# if player_input == AI_input:
#     print("平")
# elif item_input in wins:
#     print('胜')
# else:
#     print('负')
"""
    三局两胜
"""
wins = ('石头', '剪刀'
        '剪刀', '布'
        '布', '石头'
        )
item = ('石头', '剪刀', '布')
import random
win = defeat = 0
n = 1
while True:
    AI_input_number = random.randint(0, 2)
    AI_input = item[AI_input_number]
    player_input_number = int(input("第%d轮 出:石头(0)、剪刀(1)、布(2) "%n))
    if player_input_number not in range(0,3):
        print('输入有误 重新输入')
        continue
    player_input = item[player_input_number]
    print('玩家：%s  电脑:%s' % (item[player_input_number], item[AI_input_number]))
    item_input = (AI_input, player_input)
    if player_input_number == AI_input_number:
        print('平局')
        continue
    elif item_input in wins:
        win += 1
        n += 1
    else:
        defeat += 1
        n += 1
    print('胜%d次  负%d次'%(win,defeat))
    if win >2 or defeat >2:
        if win > defeat:
            print('胜')
            break
        else:
            print('负')
            break

