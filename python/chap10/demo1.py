def calc(a,b):
    c=a+b
    return c

num=calc(10, 20)
print(num)

'''函数调用后如果是不可变对象，不会更改实参的值，反之改变'''
'''
函数的返回值
(1)如果两数没有返回值【两数执行完毕之后，不需要给调用处提供数据】 return可以省略不写
(2)西数的返回值,如果是1个,直接返回类型
(3)两数的返回值,奶果是多个,返回的结果为元组(tuple)
'''