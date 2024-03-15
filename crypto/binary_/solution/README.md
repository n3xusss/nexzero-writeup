# binary?

## Write-up


this is not regular binary encoding.
we start by counting the occurances of 0's and 1's in each line 

the number of 0's in a line represents the first character in a hex byte 
while the number's of 1's do represents the 2 second byte
exemple : 

th first line is 10111100111111011100 :

number of 0's = 6
number of 1's = 14 = E

in hex 6E is equal the 'n' which is the first character of the flag : 

following this logic we find the flag : nexus{L33T_H3x_Encod3R}

here's a script that automates the solving of this challenge : 
```
f=open('flag.txt','r')
line=f.readline()
encoded=''
while line:
    encoded+=str(hex(line.count('0')))[-1]+str(hex(line.count('1')))[-1]
    line=f.readline()

print(bytes.fromhex(encoded).decode('ascii'))

```
## Flag

`nexus{L33T_H3x_Encod3R}`
