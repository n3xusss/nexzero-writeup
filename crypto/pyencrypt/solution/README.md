# Challenge name

## Write-up

after carefully reading the source code , we ee that the xor encryption is only using a 1 length key , 
`encrypted = ''.join([chr(ord(encoded_flag[i])^ord(key[0])) for i in range(len(encoded_flag))])`

which is the mistake refered to in the challenge name , so all that is left is reversing the secure_base64() function and bruteforcing the xor key 

here's a script that automates the solving of this challenge : 
```
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


```
