import os
#os.system('xx.exe') #运行win某程序
#os.startfile('/root/RemoteWorking/Computer-networking/python/chap14/demo1.py') #直接调用可执行文件
print(os.getcwd()) #查看当前操作路径

lst=os.listdir('/root/RemoteWorking/Computer-networking/python/chap14')
print(lst)