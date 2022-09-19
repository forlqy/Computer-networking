file=open('/root/RemoteWorking/Computer-networking/python/chap14/c.txt','a')
file.write('hello')
file.flush() #将缓冲区写入文件，但不关闭
file.write('world')
file.close() #写入后关闭