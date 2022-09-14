s='hello python'
print(s.replace('python', 'C++')) #字符串的替换
s1='hello,Python,Python,Python'
print(s1.replace('Python', 'C++',2))

lst=['hello','C++','Python'] #字符串的合并 列表与元组均可
print('|'.join(lst))
print(''.join(lst))