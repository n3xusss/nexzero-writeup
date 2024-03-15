# local file inclusing 1
## Write-up

local file inclusion seems to be hard , and we don't kow where the flag is at
when attempting the use lfi , it gets detected and store out infomation in a report file.
and it seems that we can use include it ! 

hmmm it stores our IP and user-agent ! 

user-agent is an information that we can control !!
so let's inject a php code like : 
`<?php echo shell_exec($_GET['cmd']) ;?>`
in our user agent and attemps a lfi.
it get stored stored in .report file , now when including the report file , 
we have achieved command injection by sending any command using the 'cmd' query 

all that's left is finding the location of flag.txt using `find` and reading it 
## Flag

`nexus{LFI2RCE?????!}`
