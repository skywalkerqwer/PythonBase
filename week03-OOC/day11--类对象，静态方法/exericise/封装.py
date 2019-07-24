"""
    面向过程方法
"""

"""
# 需求：获取指定位置上的，某个方向，指定数量的元素。
def get_elements(list_target,r_index,c_index,r_dir,c_dir,count):
    result = []
    for i in range(count):
        r_index += r_dir
        c_index += c_dir
        result.append(list_target[r_index][c_index])
    return result
# 缺点：1： 代码可读性差
#      2： 每次调用方法，都需要思考索引方向的特征
print(get_elements(list01,2,0,0,1,3))
"""

"""
    面向对象方法
"""
list01 = [
    ['00', '01', '02', '03', '04'],
    ['10', '11', '12', '13', '14'],
    ['20', '21', '22', '23', '24'],
    ['30', '31', '32', '33', '34']
]
# 使用一个类，包装两个数据（行/列）
class Vector2:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # 静态方法
    @staticmethod #不需要对象来调用函数
    def right():
        return Vector2(0,1)

def get_elements(list_target, vect_pos, vect_dir, count):
        result = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            result.append(list_target[vect_pos.x][vect_pos.y])
        return result

print(get_elements(list01,Vector2(2,0),Vector2.right(),3))



