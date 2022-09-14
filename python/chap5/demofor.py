for item in 'Python':
    print(item)

for i in range(10):
    print(i)

for _ in range(5): #下划线_不需要使用自定义变量
    print('Python')

sumOdd=0 #奇数和
sumEven=0 #偶数和
for item in range(1,101):
    if item%2:
        sumOdd+=item
    else:
        sumEven+=item
print('奇数和：',sumOdd)
print('偶数和：',sumEven)