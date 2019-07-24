print('模块--skill_deployer')

from common import list_helper

b01 = list_helper.CommonClass02()
b01.fun02()

from skill_system.skill_data import *
b02 = CommonClass11()
b02.fun11()


class CommonClass12():
    print('skill_deployer -- CLASS')

    def fun12(self):
        print('skill_deployer -- CLASS -- fun12\n')
