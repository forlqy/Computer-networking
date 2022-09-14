class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self, name, age,stu_no):
        super().__init__(name, age)
        self.stu_no=stu_no
    def info(self): #override重写 python中方法一定要与之前的方法对齐，否则被视为嵌套方法！！！
            super().info() #还想使用父类版本
            print(self.stu_no) 

class Teacher(Person):
    def __init__(self, name, age,tyear):
        super().__init__(name, age)
        self.tyear=tyear

stu=Student('张三', 20, '1001')
teacher=Teacher('梅梅', 35, 10)

stu.info()
teacher.info()

class A(object):
    pass

class B(object):
    pass
#多重继承
class C(A,B):
    pass