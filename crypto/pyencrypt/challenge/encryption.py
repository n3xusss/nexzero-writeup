import base64
import random
import string

def secure_base64(flag):
    bflag=base64.b64encode(flag.encode())
    index=1
    bflag=bflag.decode()
    encoded_flag=''

    for i in range(len(bflag)):
        encoded_flag+=bflag[i]
        for m in range(index):
            encoded_flag+= random.choice(string.ascii_letters)
        index+=1
    return encoded_flag



def encrypt(encoded_flag,key):
    encrypted = ''.join([chr(ord(encoded_flag[i])^ord(key[0])) for i in range(len(encoded_flag))])
    open('encrypted.txt','w').write(encrypted)


if __name__=="__main__":
    secret = ''.join(random.choices(string.ascii_letters, k=128)) #uncrackable 128 byte key!!!!
    flag="nexus{FAKE_FLAG}" # for testing purpose , not the real flag
    encrypt(secure_base64(flag),secret) 
