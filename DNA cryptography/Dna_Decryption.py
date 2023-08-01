import Mealy_Machine


def eor(str,key):
    trunkey = ''
    trunkey = key[-len(str):]
    exor1 = ''
    for i in range(len(trunkey)):
        if str[i] == trunkey[i]:
            exor1 += '0'
        else:
            exor1 += '1'
    return exor1

def Dna_Decryption(dna,key):

    dna=dna[::-1]
    dna= Mealy_Machine.Mealy_Machine(dna,1)
    exor=''
    #print(dna)
    for i in dna:
        if i=='A':
            exor+='10'
        if i=='T':
            exor+='01'
        if i=='C':
            exor+='00'
        if i=='G':
            exor+='11'
    #print("\ndecrypt",exor)
    str = ''
    if len(exor) <= 256:
        str = eor(exor, key)
    else:
        for k in range(0, len(exor), 256):

            str += eor(exor[k:k + 256], key)

    out=""

    for y in range(0,len(str),8):
        e=str[y:y+8]
        binary_int=int(e,2)
        out+=chr(binary_int)

    #print("result = ",Plain_Text[::-1] )
    file2=open("output.txt",'w')
    #print("plain ",Plain_Text)

    file2.write(out)
    print("\n\n\t\t------->SUCCESSFULLY DECRYPTED-------->\n\n")