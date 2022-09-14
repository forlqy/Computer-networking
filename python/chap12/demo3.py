class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #__age表示private，只能由类显式调用，不能被对象调用


stu=Student('张三', 20)
#print(stu.__age)
print(stu.name)


print(dir(stu))
print(stu._Student__age)