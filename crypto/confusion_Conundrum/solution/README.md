# Confusion Conundrum

**Difficulty:** Medium
**Category:** Crypto
**Author:** M3551
**Description:** Another one, can u decrypt it this time!    
  NB: Think out of the box!!!

## challenge.txt

```
p = 94870544634437736510840762818333376841742882634831537595688230105812017096483
q = 101676806214782912623965046172630710699952727444649297357365091181445815602423
n = 9646133982286638553098289431708359597742962890715306079129512588482795237366648221809435629553015394294363896520120846912509011493091398851884343959578309
e = 2
c = 3119764668748711508220808235240851124304269759793108959684159670352119046143946860636807179972066427531672558917069675705801167306575858295827566698345153
```

## Solution

given parameters with e = 2, the first intention will be to try RSA square root problem but it won't work, 
if we look closely to p and q we'll find that:

`p mod 4 = 3`
and
`q mod 4 = 3`

so, this is a [Rabin cryptosystem](https://en.wikipedia.org/wiki/Rabin_cryptosystem) and not RSA, 


Here is the decryption script:

```python
import math
from Crypto.Util.number import inverse

def decrypt(c, p, q):
    N = p * q
    p1 = pow(c, (p + 1) // 4, p)
    p2 = p - p1
    q1 = pow(c, (q + 1) // 4, q)
    q2 = q - q1

    gcd_pq = math.gcd(p, q)
    y_p = inverse(p // gcd_pq, q // gcd_pq)
    y_q = inverse(q // gcd_pq, p // gcd_pq)

    d1 = (y_p * p * q1 + y_q * q * p1) % N
    d2 = (y_p * p * q2 + y_q * q * p1) % N
    d3 = (y_p * p * q1 + y_q * q * p2) % N
    d4 = (y_p * p * q2 + y_q * q * p2) % N

    return d1, d2, d3, d4

def main():
    p = 94870544634437736510840762818333376841742882634831537595688230105812017096483
    q = 101676806214782912623965046172630710699952727444649297357365091181445815602423
    n = 9646133982286638553098289431708359597742962890715306079129512588482795237366648221809435629553015394294363896520120846912509011493091398851884343959578309

    c = 3119764668748711508220808235240851124304269759793108959684159670352119046143946860636807179972066427531672558917069675705801167306575858295827566698345153

    m2 = decrypt(c, p, q)
    plaintext = ""
    for b in m2:
        dec = b.to_bytes((b.bit_length() + 7) // 8, 'big').decode('ascii', errors='ignore')
        if 'nexus' in dec:
            plaintext = dec
            break

    print(plaintext)

if __name__ == "__main__":
    main()

```
## Output
nexus{r4b1n_c1ph3r_n07_RSA}aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                    
## Flag

`nexus{r4b1n_c1ph3r_n07_RSA}`