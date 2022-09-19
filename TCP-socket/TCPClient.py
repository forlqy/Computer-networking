from socket import *
serverName = '43.143.162.227' #服务器地址
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) #创建TCP套接字，IPv4 ，第一个参数为使用网络层协议，第二个为传输层
clientSocket.connect((serverName, serverPort)) #发起连接

sentence = input('Input lowercase sentence:').encode() #用户输入信息，并编码为bytes
clientSocket.send(sentence) #将信息发送至服务器
modifiedSentence = clientSocket.recvfrom(1024) #从服务器接收信息
print(modifiedSentence[0].decode()) #显示信息
clientSocket.close() #关闭套接字
#对比UDP-socket.client多了connect步骤，并且信息发送使用send而不是sendto
