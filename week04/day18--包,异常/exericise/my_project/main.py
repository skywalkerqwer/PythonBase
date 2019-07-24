"""
    main调用common/list_helper.py和 skill_system/skill_deployer
    skill_deployer调用skill_data list_helper
    要求模块中必须包含类,导包方式用from
"""
from common import double_list_helper
a01 = double_list_helper.CommonClass01()
a01.fun01()

from common.list_helper import CommonClass02
CommonClass02().fun02()


from skill_system import *
a03 = skill_data.CommonClass11()
a03.fun11()

from skill_system.skill_deployer import *
a04 = CommonClass12()
a04.fun12()

from common.sql_helper import *
a05 =CommonClass03()
a05.fun03()