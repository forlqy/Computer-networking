lst=[10,5,252,7978,34,66,89,3234]
lst.sort()
print('默认升序：',lst)
lst.sort(reverse=True)
print('降序：',lst)
lst.sort(reverse=False)
print(lst)
lst.reverse() #反转

print('--------内置函数sorted,产生新列表对象---------------')
new_list=sorted(lst)
print(lst)
print(new_list)
desc_list=sorted(lst,reverse=True)
print(desc_list)