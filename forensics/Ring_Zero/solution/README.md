# Ring Zero

## Write-up

The challenge's name and description is hinting about a rootkit, more prcesiley an LKM one. The attachment is a linux memory dump, for sure volatility is the best tool to investigate it. After building the correct volatility profile and by checking volatility linux plugins especially the ones made for malware and rootkits detection analyis we can progress in our investigation, after testing multiple plugins and  bulding the logic we conclude that the rootkit hides itself from many system files that some volatility plugins are based on, but ```linux_hidden_module``` can do the job for us (please refer to the chapter about rootkit detection analysis in The Art of Memory Forensics book to gain better understanding) and detect the hidden rootkit which is ```diamorphine.ko``` (its source code can be found in github publicly), like that we answerd the 1st question. For the core adress of the rootkit in memory we can use the ```linux_check_modules``` plugin which will give us the core adress and the module adress of the rootkit in the memory which is ```0xffffffffc067d000```. For the last question, it is the mentionned that the rootkit resulted in an execution error when giving it a specific argument, we know that our rootkit is indeed a LKM so error might be written to dmesg buffer which we can read with ```linux_dmesg``` plugin, argument name is ```crc65_key```.

Details might be added later.

Thanks,

## Flag

`nexus{diamorphine.ko_0xffffffffc067d000_crc65_key}`
