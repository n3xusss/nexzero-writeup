# Character generator

## Write-up

after carefully reading the code , we understand that we can read the flag simply by generating an admin character 

fortunately we can use the load option , 

so all there is to do , is simply creating a serialized admin_character object using pickle with the hp , attack , and defence attributes , encoding it with hexadecimal and sending it  

## Flag

`nexus{Br34K_Th3_Py_J4IL_WiTh_Cls5es}`
