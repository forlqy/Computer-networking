'''字符串的驻留机制''' 
'''1.字符串的长度为0或1；2.符合标识符的字符串;3.只在编译时驻留，而非运行时;4.[-5,256]之间整数数字'''
a='Python'
b="Python"
c='''Python'''
print(a,id(a),b,id(b),c,id(c))

d='abc%' #此时id不相等，ide做了优化，无法实验，可以到Windows内置Python3中实验
e='abc%'
#print(d is e)
#print(d.id())
#print(e.id())