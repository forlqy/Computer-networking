'''集合的数学操作'''
#求交集
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.intersection(s2))
print(s1 & s2) #&为求交集
#求并集
print(s1.union(s2))
print(s1 | s2)
#求差集
print(s1.difference(s2))
print(s1-s2)
#对称差集 ----并集-交集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

lst={i for i in range(1,10)} #集合生成式
print(lst)
