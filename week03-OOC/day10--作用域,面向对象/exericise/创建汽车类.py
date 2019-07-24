"""
    汽车类car:具有类型tpye，速度speed等数据
             启动start，停止stop，行驶run等方法
    创建两个对象：BMW Auto
"""


class Vehicle():
    def __init__(self, type, speed):
        self.type = type
        self.speed = speed

    def start(self):
        print(self.type + '\t start now')

    def stop(self):
        print(self.type + '\t stop now')

    def run(self):
        print(self.type + '\t running in ' + self.speed)


vehicle01 = Vehicle('BMW', '80')
vehicle02 = Vehicle('Auto', '85')
vehicle01.start()
vehicle01.run()
vehicle01.stop()
vehicle02.stop()