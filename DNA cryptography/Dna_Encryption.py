import Mealy_Machine

def eor(str,key):
    trunkey = ''


    trunkey = key[-len(str):]
    #print("truncate", len(trunkey))
    exor1 = ''
    for i in range(len(trunkey)):
        if str[i] == trunkey[i]:
            exor1 += '0'
        else:
            exor1 += '1'
    return exor1
def Dna_Encryption(key):
    file1=open('Plain_Text_File.txt','r')
    con=file1.readlines()
    Plain_text=""
    for g in con:
      Plain_text +=g
    str = ''
    for i in Plain_text:
        #print(bin(ord(i)).replace("0b", ''))
        a = bin(ord(i)).replace("0b", '')
        if len(a) != 8:
            for j in range(8 - len(a)):
                a = '0' + a
        str += a
    #print("str=> ", str)



    exor = ''
    if len(str) <= 256:
        exor = eor(str,key)
    else:
        for k in range(0, len(str), 256):
            exor += eor(str[k:k + 256],key)
            #print("value", k)

    #print('length', exor)

    dna = ''
    k = 1
    for i in range(0, len(exor), 2):
        if exor[i:i + 2] == '00':
            dna += 'C'
        if exor[i:i + 2] == '01':
            dna += 'T'
        if exor[i:i + 2] == '10':
            dna += 'A'
        if exor[i:i + 2] == '11':
            dna += 'G'

    file3=open("Cipher_Text.txt",'w')
    dna = Mealy_Machine.Mealy_Machine(dna,0)

    dna=dna[::-1]
    file3.write(dna)

    print("\n\n\t\t------->SUCCESSFULLY ENCRYPTED-------->\n\n")


    return dna

#  abcdefgh@gmail.com
# 0a-12-22-b4-99-66
# aeypp8436r