books=['Math','Chinese','Engish']
numbers=[1001,1002,1003,1004,1005] #若key,value个数不同，以最少的为基准
d={book.upper():number for book,number in zip(books,numbers)} #upper()函数变为大写
print(d)