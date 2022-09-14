s='hello world python'
lst=s.split() #劈分默认为空格
print(lst)

s1='hello|world|python'
print(s1.split())
print(s1.split(sep='|')) #sep指定分割符

print(s1.split(sep='|',maxsplit=1)) #maxsplit指定最大劈分次数

'''rsplit()方法从右侧开始劈分，其余与split()一致'''