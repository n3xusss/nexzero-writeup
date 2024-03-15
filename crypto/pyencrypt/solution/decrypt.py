import base64
import string
encrypted_message=open('encrypted.txt','rb').read()

for k in string.ascii_letters:
    decrypted = ''.join([chr(encrypted_message[i]^ord(k)) for i in range(len(encrypted_message))])

    if '=' in decrypted:
        print(k)
        char=''
        flag=''
        index=0
        c=2
        while char!='=':
            char=decrypted[index]
            flag+=char
            index=index+c
            c+=1

        try :
            print(base64.b64decode(flag+'=').decode())
        except:
            pass
