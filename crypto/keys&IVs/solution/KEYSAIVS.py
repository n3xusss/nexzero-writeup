from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


with open("keys&IVs.txt", "r") as file:
    lines = file.readlines()

#flag=FLAG


cipher_text=b'\xaf\xe8I\xf2\x93\xa7\x84\xb5x`ws\xafQa*\xfe\x16\xc2l\xe7p\x18\xceX\x029\x0c;\x87\xbbY=w\xed\xc0bX\xc8&\xd7\x1e\x02\x07n\x19\xc8O'



from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

for line in lines:
    for iv in lines:
        try:
            bytes_line = line.strip().encode('utf-8').decode('unicode_escape').encode('latin1')
            iv_line = iv.strip().encode('utf-8').decode('unicode_escape').encode('latin1')
            cipher = AES.new(bytes_line, AES.MODE_CBC, iv_line)
           
            decrypted_data = unpad(cipher.decrypt(cipher_text), AES.block_size)
            
            print(f"Decrypted data with key {line} and iv {iv}: {decrypted_data.decode()}")
            if b'nexus{' in decrypted_data:
                print(decrypted_data)
                break

        except ValueError as ve:
            continue


