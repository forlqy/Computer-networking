class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')


stu1=Student('张三', 19)
stu2=Student('莉丝', 20)
print('------为stu2动态绑定性别属性---------')
stu2.gender='女'
print(stu2.name,stu2.age,stu2.gender)

print('--------------')
def show():
    print('定义在类之外')
stu1.show=show
stu1.show()