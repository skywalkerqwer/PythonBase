"""
    多继承
    一个子类继承两个以上的父类，父类中的成员同时被继承
    同名方法的解析顺序(MRO)：
        类自身 --> 父类继承列表(由左至右)　--> 再上层父类
"""
"""
      A
      
  B       C
  
      D

"""
class A:
    def m01(self):
        print('A')
class B(A):
    def m01(self):
        print('B')
class C(A):
    def m01(self):
        print('C')

class D(B,C):
    def m01(self):
        super().m01()
        print('D')

d01 = D()
d01.m01()


"""
  A  B  C  D
  
   AB    CD
   
     ABCD
"""
