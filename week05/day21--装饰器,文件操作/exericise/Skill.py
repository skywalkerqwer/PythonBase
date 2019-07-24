"""
    将s01写入到文件中
    将文件中写入的内容读取到程序中，再创建Skill对象
"""


class Skill():
    def __init__(self, id=0, name='', cost_sp=0, cd=0):
        self.id = id
        self.name = name
        self.cost_sp = cost_sp
        self.cd = cd

    def __repr__(self):
        return "Skill(%d,'%s',%d,%d)" % (self.id, self.name, self.cost_sp, self.cd)


s01 = Skill(101, 's1', 5, 5)


# 将s01写入到文件中
def save_skill(target):
    with open('skill.txt', 'w', encoding='utf-8') as skill_file:
        skill_file.write(target.__repr__())


def load_skill(file_path):
    with open(file_path, 'r', encoding='utf-8') as skill_file:
        for line in skill_file:
            yield eval(line)


save_skill(s01)
for item in load_skill('skill.txt'):
    print(item)
