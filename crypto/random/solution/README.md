# Random

## Write-up

**The Mersenne Twister (MT)** is a widely-used pseudorandom number generator (PRNG) that is known for being fast and having a long period. However, there are certain properties and vulnerabilities of the Mersenne Twister that can be problematic in certain applications.  
The Mersenne Twister is not suitable for cryptographic purposes because it is not considered a cryptographically secure PRNG. Its output can be predictable if an attacker knows a sufficient number of generated values.


```python
from pwn import *
from randcrack import RandCrack

chall = remote("localhost", 1337)
#chall = process("./app.py")

rc = RandCrack()

if __name__ == "__main__":
	while True:
		chall.recvuntil(b"Take some random numbers :\n")

		# Receive the random numbers until the closing bracket
		random_numbers = eval(chall.recvuntil(b"]"))

		for r in random_numbers:
			try:
				# Submit each random number to RandCrack
				rc.submit(r)
			except:
				# If an exception occurs, it means that we have submitted enough numbers to build the state -624-
				[rc.predict_getrandbits(32) for _ in range(75)]
				chall.recv()

 		                # Send the predicted random number to the server
				chall.sendline(f"{rc.predict_getrandbits(32)}".encode())

				success(f"The flag is: {chall.recv().decode()}")
				chall.close()
				exit()

		# As we are missing the 100th number we submit 0 to RandCrack
		rc.submit(0)
		chall.sendline(b"0")
```


## Flag

`nexus{m3r53nn3_7w1573r_15_n07_cryp706r4ph1c4lly_53cur3}`
