"""
    技能系统
"""


class ImpactEffect():
    """
        影响效果
    """

    def impact(self):
        raise NotImplementedError()


class CostSpEffect(ImpactEffect):
    """
        消耗法力
    """

    def __init__(self, value):
        self.value = value

    def impact(self):
        print('消耗%s法力' % self.value)


class DamagedEffect(ImpactEffect):
    """
        伤害生命
    """

    def __init__(self, value):
        self.value = value

    def impact(self):
        print('伤害%s生命' % self.value)


class LowerSpeedEffect(ImpactEffect):
    """
        减速
    """

    def __init__(self, value):
        self.value = value

    def impact(self):
        print('降低%s速度' % self.value)


class SkillDeployer():
    """
        技能释放器
    """
    def __init__(self,name):
        # 当技能名称
        self.skill_name = name
        # 技能影响列表
        self.__impacts = []
        # 配置技能
        self.config_skill()

    def config_skill(self):
        """
            配置技能，创建技能依赖的影响效果对象
        :return:
        """
        # 读取策划的配置文件，形成数据结构(字典的值是列表　包含影响效果，　键是名字或者编号)
        dict_skill_config = {
            '降龙十八掌':['CostSpEffect(10)','LowerSpeedEffect(0.8)','DamagedEffect(20)'],
            '天下无狗':['CostSpEffect(8)','DamagedEffect(20)']
        }
        # 根据当前技能名称，获取具有的所有影响效果
        list_impact_name = dict_skill_config[self.skill_name]
        # 创建影响效果对象
        # for item in list_impact_name:
        #     self.__impacts.append(eval(item))
        self.__impacts = [eval(item) for item in list_impact_name]

    def deploy_skill(self):
        """
            释放技能
        :return:
        """
        # 遍历技能影响列表
        print('\n释放%s'%self.skill_name)

        for item in self.__impacts:
            # 执行影响算法
            item.impact()


skill01 = SkillDeployer('降龙十八掌')
skill01.deploy_skill()
skill02 = SkillDeployer('天下无狗')
skill02.deploy_skill()
