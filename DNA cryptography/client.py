import Dna_Decryption
from socket import *
import Key_Generation
from  tkinter import *


print("\n\n\t\t<--------RECEIVER SIDE------->\n\n")
s=socket(AF_INET,SOCK_STREAM)
s.bind(("",1000))

s.listen(5)

c,a=s.accept()
email=input("Enter email address   ")
mac=input("Enter MAC id  ")
pan=input("Enter PAN number  ")
print("\n\n<--------sending email address to sender.....------->")
print("<--------sending mac id to sender.....------->")
print("<--------sending pan number to sender.....------->\n\n")
c.send(bytes(  email ,'utf8'))
c.send(bytes(  mac,'utf8'))
c.send(bytes(  pan,'utf8'))



data=c.recv(45000)
Cipher_Text=data.decode()
if Cipher_Text!="":
    print("\n\n\t\t<--------CIPHER TEXT RECEIVED.....------->\n\n")
key=Key_Generation.Key_Generation(email,mac,pan)
c.close()

Dna_Decryption.Dna_Decryption(Cipher_Text,key)
