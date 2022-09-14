print('-------支持链式赋值-------')
a=b=c=20
print(id(a),id(b),id(c))
print(id(id(a)),id(id(b)),id(id(c))) #共享内存？

print('支持系列解包赋值')
z,x,c=10,20,30
print(z,x,c) #个数相同

print('swap:')
yy,xx=14,21
print('交换之前：',yy,xx)
yy,xx=xx,yy #swap
print('交换之后：',yy,xx)
