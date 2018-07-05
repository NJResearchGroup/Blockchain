import rsa
key = rsa.newkeys(512)#生成随机秘钥
privateKey = key[1]#私钥
publicKey = key[0]#公钥
print(privateKey)
print(publicKey)
message ='iamakeyforb45678,secretkeyford760'
print('Before encrypted:',message)
message = message.encode()
cryptedMessage = rsa.encrypt(message, publicKey)
# cryptedMessage1 = cryptedMessage.decode('utf-8')
print('After encrypted:\n',cryptedMessage)
message = rsa.decrypt(cryptedMessage, privateKey)
message = message.decode()
print('After decrypted:',message)