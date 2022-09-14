lst=[10,20,30,40,50,60,70,80]
print('原列表',id(lst))
lst2=lst[1:6:1]
lst3=lst[1:6] #默认步长为1
lst4=lst[1:6:] #:后不写也为1
print('切的列表',id(lst2))
print(lst2) #lst[start,end,step]
print(lst3)
print(lst4)
print(lst[:6:2]) #start默认0
print(lst[1::2]) #end默认到尾部
print('-------step为负数---------')
print(lst[::-1]) #逆序输出
print(lst[7::-1]) #步长为负，默认start与end颠倒