a=10
b=10

print(a==b) #比较值用==
print(a is b) #比较标识用is

print('数组')
lst1=[1,2,33,4]
lst2=[1,2,33,4]
print(lst1==lst2)
print(lst1 is lst2)
print(id(lst1),id(lst2))
print(lst1 is not lst2)
