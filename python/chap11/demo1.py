try:
    n1=int(input('输入一个整数'))
    n2=int(input('输入另一个整数'))
    result=n1/n2
    print('结果：',result)
except ZeroDivisionError:
    print('除数不能为0哦')
except ValueError:
    print('只能为数字串')
print('程序结束')