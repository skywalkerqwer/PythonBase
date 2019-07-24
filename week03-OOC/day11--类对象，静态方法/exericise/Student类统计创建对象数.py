class Student():
    count = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.count += 1

    @classmethod
    def get_count(cls):
        print(cls.count)


s01 = Student('zs', 100)
s02 = Student('ls', 99)
s03 = Student('ww', 98)
Student.get_count()
