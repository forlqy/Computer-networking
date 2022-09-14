s={1,2,3,4,5}
s1={5,4,3,2,1}
print(s==s1)
print(s!=s1) 

#一个集合是否为另一个的子集
s2={2,3,4}
s3={1,2,9}
print(s2.issubset(s1))
print(s3.issubset(s1))
#是否为超集
print(s1.issuperset(s2))
#两个集合是否含有交集
print(s2.isdisjoint(s3))
s4={100,2000,300}
print(s2.isdisjoint(s4)) #没有交集为True