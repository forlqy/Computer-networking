def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

fun(10, 20, 30)
lst=[11,23,43]
fun(*lst) 
print('-----------')
fun(a=10, b=20, c=30)

dic={'a':111,'b':222,'c':333}
#fun(dic) error
fun(**dic)


def fun():
    global ll #在函数内部用global声明的为全局变量