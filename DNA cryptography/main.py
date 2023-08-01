
import Key_Generation
import Dna_Encryption
import Dna_Decryption


print("\n\n\t\t<--------SENDER SIDE------->\n\n")

from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.connect(("localhost",1000))

email=s.recv(45000)
mac=s.recv(45000)
pan=s.recv(45000)
print("\n\n<--------receiving email address from receiver.....------->")
print("<--------receiving mac id from receiver.....------->")
print("<--------receiving pan number from receiver.....------->\n\n")
email=email.decode()
mac=mac.decode()
pan=pan.decode()
key=Key_Generation.Key_Generation(email,mac,pan)
Cipher_Text=Dna_Encryption.Dna_Encryption(key)
s.send(bytes(   Cipher_Text  ,'utf8'))
#Dna_Decryption.Dna_Decryption(Cipher_Text,key)
s.close()
