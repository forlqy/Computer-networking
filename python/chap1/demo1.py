print('hello world')
#将数据输出到文件中
fp=open('/root/RemoteWorking/Computer-networking/Computer-networking/UDP-socket/test.text', 'a+')
#a+ 若文件不存在，创建文件,存在->附加到文件尾部
print('helloworld',file=fp)#一定要有file
fp.close()
#不进行换行输出
print('hello','world','python')