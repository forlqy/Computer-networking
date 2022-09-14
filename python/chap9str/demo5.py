s='hello,world'
print('1',s.isidentifier()) #判断是否为合法标识符
print('2','hello'.isidentifier())

print('3','\t'.isspace()) #判断是否为空白字符：空格,回车,换行

print('4','abc'.isalpha()) #判断字符串是否全部由字母组成
print('5','张三'.isalpha())

print('6','123'.isdecimal()) #判断是否由十进制数字组成

print('7','10010011'.isnumeric()) #判断是否为数字，汉字与罗马数字也为True
print('8','123四'.isnumeric())

print('9','abc1'.isalnum()) #判断是否由字母和数字组成
print('10','张三123'.isalnum())
print('11','abc!'.isalnum())