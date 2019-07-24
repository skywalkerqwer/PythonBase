"""
    玩家(具有攻击力)攻击敌人，敌人(具有血量)受伤后掉血，还可能死掉。
    敌人攻击玩家，玩家受伤后掉血并碎屏，还可能死亡(游戏结束)
"""


class Player:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    def attack(self, enemy):
        print('玩家进行攻击')
        enemy.damage(self.atk)

    def damage(self, value):
        print('玩家扣血')
        self.hp -= value
        if self.hp <= 0:
            self.__death()
        print('碎屏')

    def __death(self):  # 私有的方法　类外无法调用
        print('GameOver')


class Enemy:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    def attack(self, player):
        print('敌人进行攻击')
        player.damage(self.atk)

    def damage(self, value):
        self.hp -= value
        print('敌人扣血')
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print('敌人死亡')


p01 = Player(10, 100)
e01 = Enemy(5, 50)
e01.attack(p01)
p01.attack(e01)
