class A(object):
    pass

class B(object):
    pass

class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age

x=C('Jack', 20)
print(x.__dict__) #实例对象的属性字典
print('----------------')
print(C.__dict__)
print('-----------------')
print(x.__class__) #对象所属的类
print(C.__bases__) #输出父类元组（多重继承）
print(C.__base__) #多重继承的第一个父类
print(C.__mro__) #类的层次结构
print('***********')
print(A.__subclasses__()) #__subclasses()后跟小括号是个方法 输出A的子类列表