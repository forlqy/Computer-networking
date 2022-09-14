s={10,20,30,40,505,34}
print(20 in s)
print(30 not in s)
#集合元素新增操作
s.add(88)
print(s)
s.update({200,300}) #添加多个用update
s.update([123,321])
s.update((99,807))
print(s)
#集合元素删除操作
print('删除')
s.remove(505)
#s.remove(666) #抛出KeyError异常
print(s)
s.discard(300)
s.discard(999) #即使没有此元素，也不会报错
print(s)
s.pop() #一次删除一个任意元素
s.pop() #不能指定参数，否则抛出异常TypeError
print(s)
s.clear() #清空
print(s)