lst=['hello','world',10]
print(id(lst))
print(type(lst))
print(lst)

lst2=list(['hello','world',10])
print(lst==lst2)
print(id(lst2))
print(type(lst2))
print(lst2)

print(lst2[1],lst2[-2]) #负数从列表尾部的下一个哨兵开始往前数