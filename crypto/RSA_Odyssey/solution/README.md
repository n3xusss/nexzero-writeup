# RSA_Odyssey

**Difficulty:** Medium
**Category:** Crypto
**Author:** M3551
**Description:** I've encrypted a flag using RSA, confident in its unbreakable security. But can you prove me wrong?


## Solution

Connecting to the nc link we find an oracle that gives us a ciphertext c encrypted with RSA with the parameters n and e, and a message telling us to enter a ciphertext to decrypt it, but if we try to enter the encrypted flag, we'll get `Unauthorized!!!!!!!!`

The idea here is to exploit the homomorphic caracteristic of RSA to decrypt the flag. 
[here](https://www.youtube.com/watch?v=r8psTgL4K4M)

So all we have to do is writing the c in the format of c = a * b then we'll have:

`D(c) = D(a * b) mod n = D(a) * D(b) mod n`

Here is an example of how to do this with python:

```python
from Crypto.Util.number import *

n =  5274757153950277849838954215394737695545346177619588955840872416229975365254500782515740092229443505419859946549771252796561846506850879126222747503271389
e =  65537
c =  2274746470661323416430378473202697646582012177877133179569870923324636753393628859011202591859517567310540802592590772100905170950418773482647820501547018

# in this case we have c is a pair number so we have c = 2x
a = c //2 # a = 1137373235330661708215189236601348823291006088938566589784935461662318376696814429505601295929758783655270401296295386050452585475209386741323910250773509

b = 2

#decrypted a
d_a = 5214968932934523187609821375580451615116450860914601254112397387642139472510826496413493228085146099009605557798801461914921855136217332093469876253791558

#decrypted b
d_b = 4859149010497540249539248596846966730657021307858467605554641571703115555321885622528562367714369413778015084239319062527833166444501639203178256517479460


flag = (d_a * d_b) % n

print(long_to_bytes(flag))
```
## Output
b'nexus{H0m0m0rph1sm_4nd_Cryp70_4r3_4w3s0m3}'
                    
## Flag

`nexus{H0m0m0rph1sm_4nd_Cryp70_4r3_4w3s0m3}`