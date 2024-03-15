f=open('flag.txt','r')
line=f.readline()
encoded=''
while line:
    encoded+=str(hex(line.count('0')))[-1]+str(hex(line.count('1')))[-1]
    line=f.readline()

print(bytes.fromhex(encoded).decode('ascii'))











