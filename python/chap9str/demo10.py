s='人生得意须尽欢'
print(s.encode(encoding='GBK')) #一个中文占2字节
print(s.encode(encoding='UTF-8')) #中文占3字节

#解码
byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))
#print(byte.decode(encoding='GBK')) #失败
print(byte.decode())