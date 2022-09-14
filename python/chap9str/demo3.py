'''字符串的对齐'''
s='hello,world'
#居中
print(s.center(20,'*'))
print(s.center(20))
#左对齐
print(s.ljust(20,'*'))
print(s.ljust(20))
print(s.ljust(10))
#右对齐
print(s.rjust(20,'*'))
print(s.rjust(20))
#右对齐，0填充
print(s.zfill(20))

print('-8910'.zfill(8)) #-号占5个0