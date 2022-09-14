from socket import *
serverName = '43.143.162.227' #服务器地址
serverPort = '12000' #服务器指定端口
clientSocket = socket(AF_INET, SOCK_DGRAM) #创建UDP套接字，使用IPv4协议
message = input('Input lowercase sentence:').encode() #用户输入信息，并编码为bytes以便发送
clientSocket.sendto(message, (serverName, serverPort)) #将信息发送到服务器
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #从服务器接收信息，同时得到服务器地址
print(modifiedMessage.decode()) #显示信息
clientSocket.close() #关闭套接字