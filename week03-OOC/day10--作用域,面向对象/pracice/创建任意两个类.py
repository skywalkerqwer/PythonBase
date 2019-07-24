"""
    创建2个类 -- 任何类
"""


class Buliding():
    """建筑类"""
    def __init__(self, name,  floor, space):
        self.name = name
        self.space = space
        self.floor = floor

    def state(self):
        print(self.name+'is in service')

    def describe(self):
        print('Buliding\t'+self.name+' have '+self.floor+' floors '
              +'covers '+self.space+' square meters')


class Fish():
    def __init__(self,breed,weight,producing_area):
        self.breed = breed
        self.weight = weight
        self.producing_area = producing_area

    def describe(self):
        print('This '+self.weight+' '+self.breed+' produts from '+self.producing_area.title())


bulid01 = Buliding('协和医院','10','50000')
bulid01.state()
bulid01.describe()
fish01 = Fish('salmon','10kg','tokai')
fish01.describe()