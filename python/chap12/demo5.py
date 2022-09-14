class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self): #重写object类的__str__方法
        return '我的名字是{0}，我的年龄是{1}岁'.format(self.name,self.age)    

stu=Student('张三',20)
print(dir(stu))
print(stu)