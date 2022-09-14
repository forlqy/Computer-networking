'''集合的创建方式'''
#1
s={2,2,3,4,5,5,6,7,8,9,9}
print(s) #集合中不能出现重复元素，自动去重 （value,value）

#2内置函数set()
s1=set(range(5))
print(s1,type(s1))

s2=set([2,3,4,9,7,99,2,6])
print(s2,type(s2)) #集合中的元素无序

s3=set((3,4,5,67,82,1,4))
print(s3,type(s3))

s4=set('python')
print(s4)

s5=set({2,3,5,7,9})
print(s5)

#定义空集合
s6={} #不可以直接使用{} 为dict
print(type(s6))

s7=set()
print(type(s7))