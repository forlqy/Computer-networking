for i in range(3):
    pw=input('请输入密码：')
    if pw=='6666':
        print('密码正确')
        break
    else:
        print('密码错误，清再试一次')
else:
    print('三次机会已过')


a=0
while a<3:
    pw=input('请输入密码：')
    if pw=='6666':
        print('密码正确')
        break
    else:
        print('密码错误，清再试一次')
        a+=1
else:
    print('三次机会已过')