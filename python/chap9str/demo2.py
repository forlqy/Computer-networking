'''字符串的查询操作'''
s='hello,hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))

#print(s.index('k')) #抛ValueError异常
print(s.find('k')) #返回-1