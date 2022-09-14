money=1000
s=int(input('请输入取款金额:'))
if s<=money:
    money-=s
    print('取款成功，余额为：',money)



num=int(input('请输入一个整数：'))
if num%2==0:
    print(num,'是偶数')
else:
    print(num,'是奇数')

score=int(input('输入成绩：'))
if score>=90 and score<100:
    print('A')
elif 80<=score<90:  #python可以连续判断
    print('B')
else:
    print("C以下")