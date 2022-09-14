try:
    n1=int(input('输入一个整数'))
    n2=int(input('输入另一个整数'))
    result=n1/n2
except BaseException as e:
    print('出错了',e)
else:
    print('结果：',result)
finally: #无论是否出错都会执行
    print('谢谢您的使用')