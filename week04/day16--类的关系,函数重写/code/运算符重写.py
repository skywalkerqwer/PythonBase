class Vector:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        # return self.x +other
        return Vector(self.x + other)

    def __rsub__(self, other):
        return Vector(other - self.x)

    def __mul__(self, other):
        return self.x * other

    def __rpow__(self, other):
        return other ** self.x

    def __iadd__(self, other):
        self.x += other
        return self.x

    def __imul__(self, other):
        self.x *= other
        return self.x

    def __isub__(self, other):
        self.x -= other
        return self.x

    def __itruediv__(self, other):
        self.x /= other
        return self.x

    def __lt__(self, other):
        return self.x < other

    def __gt__(self, other):
        return self.x > other

    def __eq__(self, other):
        return self.x == other

    def __ne__(self, other):
        return self.x != other

    def __str__(self):
        return '%d' % self.x


v01 = Vector(1) + 2
v02 = 1 - Vector(2)
v03 = Vector(4) * 5
v04 = 4 ** Vector(2)
print(v01)
print(v02)
print(v03)
print(v04)
# 只有__add__也可以使用+=　但是会创建新变量　销毁旧变量
v05 = Vector(1)
v05 += 2
print(v05)
v06 = Vector(4)
v06 *= 2
print(v06)
v06 -= 2
print(v06)
v06 /= 3
print(v06)
print(v06 < 10)
print(v06 > 5)
print(v06 == 1)
print(v06 != 1)