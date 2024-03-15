# ame server

## Write-up

let's exploit a misconfiguration in that the domaine name server called zone tranfer , we trick the server to transfer the one the nexus-security-club.com to us 
`dig @102.220.29.203 -p4500 nexus-security-club.com axfr` 
we find a secret CNAME record pointing to an onion hidden server
fire up TOR and retrieve your flag from the dark web 

## Flag

`nexus{d4rk_WeB_Do3snt_Us3_dNS_r1GHt?}`
