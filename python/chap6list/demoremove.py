lst=[10,20,30,40,50,60,30]
lst.remove(30)
print(lst)
#lst.remove(100) ValueError:x not in list

#pop()根据索引移除元素
lst.pop(1)
print(lst)
#lst.pop(5) IndexError:pop index out of range
lst.pop() #若不写参数，删除最后一个元素
print(lst)

print('----------切片，删除至少一个，但产生新列表对象--------------')
new_list=lst[1:3]
print('原列表',lst)
print('切片之后：',new_list)
'''不产生新列表对象'''
lst[1:3]=[]
print(lst)
'''清楚列表中所有元素'''
lst.clear()
print(lst)
#del语句直接删除列表对象
del lst
#print(lst) 'lst' is not defined


lst1=[10,20,30,40]
lst1[1:3]=[300,400,500,600]
print(lst1)
