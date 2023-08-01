def zigzag_model(em,pn):
    z = []
    for i in range(len(em)):
        if i < len(pn):
            z.append(pn[i])
        if i < len(em):
            z.append(em[i])
    return z

def rask_trun(bn):
    if len(bn)>=256:
        rask = bn[:256]
    else:
        rask=bn
        for i in range(0,256-len(bn)):
            rask="0"+rask
    return rask

def binary_convert(z):
    bn = ""
    for i in z:
        bn += bin(i)[2:].zfill(8)
    return bn

def ascci_value(em):
    for i in range(len(em)):
        em[i]=ord(em[i])
    return em


def email_mac(email,mac):
    email_mac=email+mac
    email_mac=email_mac.replace("-","")
    return email_mac

def Key_Generation(email,mac,pan):

    emailmac=email_mac(email,mac)
    emailmac=list(emailmac)
    panid=list(pan)
    emailmac=ascci_value(emailmac)
    panid= ascci_value(panid)
    zigzag=zigzag_model(emailmac,panid)

    binary=binary_convert(zigzag)

    rask=rask_trun(binary)

    return rask







#Key_Generation("abcdefgh@gmail.com","0a-12-22-b4-99-66","aeypp8436r")