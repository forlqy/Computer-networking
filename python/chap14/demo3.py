src_file=open('/root/RemoteWorking/Computer-networking/python/chap14/src.png','rb') #'b'表示以二进制格式读写，必须配合r or w使用

target_file=open('/root/RemoteWorking/Computer-networking/python/chap14/goto.png','wb')

target_file.write(src_file.read())

target_file.close()
src_file.close() #图片复制