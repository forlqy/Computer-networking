print('hello\nworld')
print('hello\tworld')
print('helloooo\tworld')#\t 4个字符对齐
print('hello\rworld')
print('hello\bworld')

print('http:\\\\www.baidu.com')#\ 转义字符
print('张奎天:\'我是你爹\'')

#原字符，不希望转义字符起作用，在''前加上r或R
print(r'hello\nworld')
#tips:最后一位不能为\
#print(r'hello\nworld\')
print(r'hello\nworld\\')