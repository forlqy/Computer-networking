lst=[10,20,30]
print('添加前：',lst,id(lst))
lst.append(100)
print('添加后：',lst,id(lst))
#添加多个元素
lst2=['hello','world']
lst.extend(lst2) #将lst2作为一个元素加入lst末尾
print(lst)
#在列表任何位置添加一个元素
lst.insert(1, 90)
print(lst)
#在任意位置添加n个元素 （切片）
lst3=[True,False,'Hello','world']
lst[1:]=lst3 #把原lst索引>1的切掉，lst3加入尾部
print(lst)