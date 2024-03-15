# Exfiltration Pro Max

## Write-up

tshark -r capture.pcapng -Y "ip.src==192.168.177.137 && tcp.srcport==7035 && ip.dst==137.177.168.192 && tcp.dstport==5380" -T fields -e tcp.flags | cut -c 5- | sed '1,2d' | xxd -r -p > file.zip

zip archive is password protected, we need to crack it: 
fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt file.zip
password found: california

Unzip the archive and you get 03 files: flag.txt flag.png resume.docx
flag.txt and flag.png are just trash, nothing interesting in them, while resume.docx and when open it looks suspicious since you can't see the content and it is all whitespace except the eitle but you can select it and copy it, it looks like whitespace languagel, using https://www.dcode.fr/whitespace-language , you paste the the whitespace and finally you get:

Name: John Doe
Age: 1337
Address: Los Angeles
Team: Plaid Parliament of Forensics
Skills: pwn, forensics
Slogan: Following the trail of bits
Flag: nexus{D4TA_Exfl1tr4ti0n_Via_TCP_Flags$$$}

Note: detailed writeup might be added later.

## Flag

`nexus{D4TA_Exfl1tr4ti0n_Via_TCP_Flags$$$}`
