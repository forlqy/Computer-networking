ans=input('您是会员吗？y/n')
money=int(input('您的消费为：'))

if ans=='y':
    if money>=300:
        print('8折后为：',money*0.8)
    elif money>=200 and money<300:
        print('9折后为：',money*0.9)
    else:
        print('懒得写了')
else:
    if money>=300:
        print('9.5折：',money*0.95)
    else:
        print(money)