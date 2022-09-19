with open('/root/RemoteWorking/Computer-networking/python/chap14/src.png','rb') as src_file:
    with open('/root/RemoteWorking/Computer-networking/python/chap14/target.png','wb') as target_file:
        target_file.write(src_file.read())