#range()的三种创建方式（迭代器？）
'''第一种创建方式，只有一个参数'''
r=range(10) #默认从0开始，默认步长为1
print(r)
print(list(r)) #用于查看range对象中的整数序列

'''第二种'''
r=range(1,10) #range(start,stop)
print(r)
print(list(r))

'''第三种'''
r=range(1,10,2)
print(r)
print(list(r))

#判断指定整数是否存在于序列
print(9 in r)
print(10 in r)