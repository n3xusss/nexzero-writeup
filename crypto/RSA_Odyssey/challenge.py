from Crypto.Util.number import *

flag = bytes_to_long(b"nexus{H0m0m0rph1sm_4nd_Cryp70_4r3_4w3s0m3}")

p = getPrime(256)
q = getPrime(256)
n = p*q
e = 65537

c = pow(flag, e, n)
phi = (p-1) * (q-1)
d = inverse(e, phi)

print("n = ", n)
print("e = ", e)
print("c = ", c)

while True:
    ciphertext = int(input("Enter your ciphertext de decrypt it  : \n"))
    plaintext = pow(ciphertext, d, n)
    if (plaintext == flag):
        print("Unauthorized!!!!!!!!")
    else:
        print("The plaintext is :", plaintext)
        print(long_to_bytes(plaintext))
