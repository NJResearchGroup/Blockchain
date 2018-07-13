import rsa
from binascii import b2a_hex
key = rsa.newkeys(512)#生成随机秘钥
privateKey = key[1]#公钥+私钥
publicKey = key[0]#公钥
print(privateKey)
print(publicKey)
message ='iamakeyforb45678,secretkeyford760' #加密内容(在实验中可修改，但注意加密字符长度，根据官网文档，512bit的秘钥可以加密53bytes的字符 p.s.本来是64bytes,其中11bytes做了随机填充)
print('Before encrypted:',message)
message = message.encode()
cryptedMessage = rsa.encrypt(message, publicKey)  #对message进行加密
cryptedMessage_hex = b2a_hex(cryptedMessage)	#将密文转化为16进制字节码，方便在终端输出
print('After encrypted:\n',cryptedMessage_hex)		#加密后的密文
message = rsa.decrypt(cryptedMessage, privateKey)
message = message.decode()                     #解密后的密文
print('After decrypted:',message)
