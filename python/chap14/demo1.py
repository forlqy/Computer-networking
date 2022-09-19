file=open('/root/RemoteWorking/Computer-networking/python/chap14/a.txt','r') 
 #后面还可以跟第三个参数确定编码格式
#print(file.readlines()) #返回列表
print(file.readline()) #读取一行
#print(file.read())
print(file.read(2)) #读取几个字符
file.close()
