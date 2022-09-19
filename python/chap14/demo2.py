file=open('/root/RemoteWorking/Computer-networking/python/chap14/b.txt','w') 
print(file.write('helloworld')) #返回列表

print(file.write('python'))
file.close()

file1=open('/root/RemoteWorking/Computer-networking/python/chap14/b.txt','a') #'a'追加文本
file1.write('xuexue')
file1.close()