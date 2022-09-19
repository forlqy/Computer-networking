file=open('/root/RemoteWorking/Computer-networking/python/chap14/a.txt','r')
file.seek(3) #这里一个汉字通过utf-8编码占3字节，所以要写三的倍数作为文件起始指针，不然会报错
print(file.read())
print(file.tell()) #返回文件尾部指针
file.close()