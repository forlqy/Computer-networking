class Student:
    native_pace='吉林'
    def __init__(self,name,age):
        self.name=name #self.name称为实例属性
        self.age=age
    #实例方法
    def eat(self):
        print('学生在吃饭')

    #静态方法
    @staticmethod
    def method():
        print('我是静态方法')

    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，参数为cls')

#类之外称为函数，类内为方法
def drink():
    print('喝水')

'''创建类对象'''
stu1=Student('张三', 20)
print(id(stu1))
print(type(stu1))
print(stu1) #与id输出的值相等，一个十进制一个十六进制
print('----------------')
print(id(Student))
print(type(Student))
print(Student) 
'''下面两行完全等效'''
stu1.eat()
Student.eat(stu1)
#静态和类方法痛过类名使用
Student.cm()
Student.method()